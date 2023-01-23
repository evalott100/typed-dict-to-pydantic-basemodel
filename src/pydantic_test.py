from pathlib import Path
from pydantic.dataclasses import dataclass
import json
from typing import TypedDict, Annotated, List, Dict, Any, Type, _TypedDictMeta
from pydantic import create_model, BaseModel as PydanticBaseModel, Field

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


def desc(description: str):
    return Field(description=description)


def title(title: str):
    return Field(title=title)


def additionalProperties(additional_properties: bool):
    return Field(additional_properties=additional_properties)


class BulkDatum(TypedDict):
    # The docstring functions as the description field.
    """Document to reference a quanta of externally-stored data"""

    datum_kwarg_list: Annotated[
        List[object],
        desc(
            "Array of arguments to pass to the Handler to retrieve one quanta of data"
        ),
    ]

    resource: Annotated[
        str,
        desc("UID of the Resource to which all these Datum documents belong"),
    ]

    datum_ids: Annotated[
        List[str],
        desc(
            "Globally unique identifiers for each Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'"
        ),
    ]


class Config:
    additional_properties = False


# From https://github.com/pydantic/pydantic/issues/760#issuecomment-589708485
def parse_dict(typed_dict: _TypedDictMeta) -> Type[PydanticBaseModel]:
    annotations = {}
    for name, field in typed_dict.__annotations__.items():
        if isinstance(field, _TypedDictMeta):
            annotations[name] = (parse_dict(field), ...)
        else:
            default_value = getattr(typed_dict, name, ...)
            annotations[name] = (field, default_value)

    model = create_model(typed_dict.__name__, **annotations)

    @dataclass(config=Config)
    class ModelClass(model):
        ...

    return ModelClass


def export_json_schema(
    typed_dict: _TypedDictMeta, path: Path = Path("gen_bulk_datum.json")
):
    model = parse_dict(typed_dict)

    # Use the docstring of the TypedDict as the json schema description.
    model.__doc__ = typed_dict.__doc__

    with open(path, "w+") as f:
        json.dump(model.schema(), f, indent=3)


export_json_schema(BulkDatum)
