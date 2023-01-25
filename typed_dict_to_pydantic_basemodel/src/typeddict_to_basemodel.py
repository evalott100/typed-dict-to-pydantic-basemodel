from pathlib import Path
import re
import json
from pydantic import create_model, BaseModel, Field, Extra
from typing import Type, _TypedDictMeta


def snake_case(string: str) -> str:
    return "_".join(
        re.sub(
            "([A-Z][a-z]+)",
            r" \1",
            re.sub("([A-Z]+)", r" \1", string.replace("-", " ")),
        ).split()
    ).lower()


# Config for generated BaseModel
class Config(BaseModel.Config):
    extra = Extra.forbid
    alias_generator = snake_case
    allow_population_by_field_name = True


# From https://github.com/pydantic/pydantic/issues/760#issuecomment-589708485
def parse_dict(typed_dict: _TypedDictMeta) -> Type[BaseModel]:
    annotations = {}

    for name, field in typed_dict.__annotations__.items():
        if isinstance(field, _TypedDictMeta):
            annotations[name] = (parse_dict(field), ...)
        else:
            default_value = getattr(typed_dict, name, ...)
            annotations[name] = (field, default_value)

    model = create_model(typed_dict.__name__, **annotations, __config__=Config)

    # Docstring is used as the description field.
    model.__doc__ = typed_dict.__doc__

    # title goes to camelcase
    model.__name__ = snake_case(typed_dict.__name__)
    return model


def export_typedict_to_json_schema(
    typed_dict: _TypedDictMeta, out_dir: Path | None = None
):
    model = parse_dict(typed_dict)

    # Use the docstring of the TypedDict as the json schema description.

    if out_dir:
        with open(out_dir / f"{model.__name__}.json", "w+") as f:
            json.dump(model.schema(by_alias=True), f, indent=3)

    return dict(model.schema(by_alias=True))
