from pathlib import Path
import re
import json
from pydantic import create_model, BaseModel, Extra
from typing import Type, _TypedDictMeta
from apischema.json_schema import deserialization_schema
from apischema.utils import to_snake_case


# Config for generated BaseModel
class Config(BaseModel.Config):
    extra = Extra.forbid
    alias_generator = to_snake_case
    allow_population_by_field_name = True


# From https://github.com/pydantic/pydantic/issues/760#issuecomment-589708485
def parse_dict_to_pydantic_basemodel(typed_dict: _TypedDictMeta) -> Type[BaseModel]:
    annotations = {}

    for name, field in typed_dict.__annotations__.items():
        if isinstance(field, _TypedDictMeta):
            annotations[name] = (parse_dict_to_pydantic_basemodel(field), ...)
        else:
            default_value = getattr(typed_dict, name, ...)
            annotations[name] = (field, default_value)

    model = create_model(typed_dict.__name__, **annotations)

    # Docstring is used as the description field.
    model.__doc__ = typed_dict.__doc__

    # title goes to camelcase
    model.__name__ = to_snake_case(typed_dict.__name__)
    return model.schema(by_alias=True)


# From https://github.com/pydantic/pydantic/issues/760#issuecomment-589708485
def parse_dict_to_apischema(typed_dict: _TypedDictMeta) -> dict:
    model = deserialization_schema(typed_dict)

    # Docstring is used as the description field.
    model["description"] = typed_dict.__doc__

    # title goes to camelcase
    model["title"] = to_snake_case(typed_dict.__name__)
    return model


def export_typedict_to_json_schema(
    typed_dict: _TypedDictMeta, out_dir: Path | None = None
):
    model = parse_dict_to_apischema(typed_dict)
    model["description"] = typed_dict.__doc__
    model["title"] = to_snake_case(model["title"]).lower()

    # Use the docstring of the TypedDict as the json schema description.

    if out_dir:
        with open(out_dir / f'{model["title"]}.json', "w+") as f:
            json.dump(model, f, indent=3)

    return dict(model)
