from pathlib import Path
import re
import json
from pydantic import create_model, BaseModel, Field, Extra

SCHEMA_DIR = Path("src/schemas")

bulk_datum_dict = json.load(Path(SCHEMA_DIR / "bulk_datum.json").open())
bulk_events_dict = json.load(Path(SCHEMA_DIR / "bulk_events.json").open())
datum_page_dict = json.load(Path(SCHEMA_DIR / "datum_page.json").open())
datum_dict = json.load(Path(SCHEMA_DIR / "datum.json").open())
event_descriptor_dict = json.load(Path(SCHEMA_DIR / "event_descriptor.json").open())
event_dict = json.load(Path(SCHEMA_DIR / "event.json").open())
event_page_dict = json.load(Path(SCHEMA_DIR / "event_page.json").open())
resource_dict = json.load(Path(SCHEMA_DIR / "resource.json").open())
run_start_dict = json.load(Path(SCHEMA_DIR / "run_start.json").open())
run_stop_dict = json.load(Path(SCHEMA_DIR / "run_stop.json").open())
stream_datum_dict = json.load(Path(SCHEMA_DIR / "stream_datum.json").open())
stream_resource_dict = json.load(Path(SCHEMA_DIR / "stream_resource.json").open())


from typing import Type, _TypedDictMeta


def snake_case(string: str) -> str:
    return "_".join(
        re.sub(
            "([A-Z][a-z]+)",
            r" \1",
            re.sub("([A-Z]+)", r" \1", string.replace("-", " ")),
        ).split()
    ).lower()


class Config(BaseModel.Config):
    extra = Extra.forbid
    alias_generator = snake_case


# From https://github.com/pydantic/pydantic/issues/760#issuecomment-589708485
def parse_dict(typed_dict: _TypedDictMeta) -> Type[BaseModel]:
    annotations = {}

    for name, field in typed_dict.__annotations__.items():
        print("")
        print(name)
        print(field)
        print("")
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


def export_json_schema(typed_dict: _TypedDictMeta, out_root: Path = Path("out")):
    model = parse_dict(typed_dict)

    # Use the docstring of the TypedDict as the json schema description.

    with open(out_root / f"{model.__name__}.json", "w+") as f:
        json.dump(model.schema(by_alias=True), f, indent=3)


from type_dict_definitions import BulkDatum

export_json_schema(BulkDatum)
