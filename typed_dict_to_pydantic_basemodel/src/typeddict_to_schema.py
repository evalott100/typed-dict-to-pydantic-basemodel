from pathlib import Path
import re
import json
from pydantic import create_model, BaseModel, Extra
from typing import Type, _TypedDictMeta, Optional


# Config for generated BaseModel
class Config(BaseModel.Config):
    extra = Extra.forbid

    # Alias in snake case
    alias_generator = lambda x: re.sub(r"(?<!^)(?=[A-Z])", "_", x).lower()


# From https://github.com/pydantic/pydantic/issues/760#issuecomment-589708485
def parse_dict_to_pydantic_basemodel(
    typed_dict: _TypedDictMeta, out_dir: Optional[Path] = None
) -> Type[BaseModel]:
    annotations = {}

    for name, field in typed_dict.__annotations__.items():
        if isinstance(field, _TypedDictMeta):
            annotations[name] = (parse_dict_to_pydantic_basemodel(field), ...)
        else:
            default_value = getattr(typed_dict, name, ...)
            annotations[name] = (field, default_value)

    model = create_model(typed_dict.__name__, **annotations, __config__=Config)

    # Docstring is used as the description field.
    model.__doc__ = typed_dict.__doc__

    # title goes to camelcase
    model.__name__ = Config.alias_generator(typed_dict.__name__).lower()
    model_schema = model.schema()

    model_schema["description"] = typed_dict.__doc__

    if out_dir:
        with open(out_dir / f'{model_schema["title"]}.json', "w+") as f:
            json.dump(model_schema, f, indent=3)

    return model_schema
