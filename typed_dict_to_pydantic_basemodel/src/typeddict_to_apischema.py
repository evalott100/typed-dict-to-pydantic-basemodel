from apischema.json_schema import deserialization_schema, JsonSchemaVersion
from pathlib import Path
from typing import TypedDict
import json


def get_json_from_typeddict(typed_dict: TypedDict, out_dir: Path | None = None):
    deserialized = deserialization_schema(
        typed_dict.__annotations__
    )  # , version=JsonSchemaVersion.DRAFT_7)
    # deserialized["description"] == typedict.__doc__
    if out_dir:
        with open(out_dir / (typed_dict.__name__ + ".json"), "w+") as file:
            json.dump(deserialized, file, indent=3)
    return deserialized


with open("typed_dict_to_pydantic_basemodel/schemas/bulk_datum.json", "r") as f:
    json_contents = json.load(f)
    print(TypedDict("bulk_datum", json_contents["properties"]))
