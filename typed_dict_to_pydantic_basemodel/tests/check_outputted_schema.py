from typed_dict_to_pydantic_basemodel.src.typeddict_to_basemodel import (
    export_typedict_to_json_schema,
)

from typed_dict_to_pydantic_basemodel.src.models.datum_page import DatumPage
from typed_dict_to_pydantic_basemodel.src.models.datum import Datum
from typed_dict_to_pydantic_basemodel.src.models.event_descriptor import EventDescriptor
from typed_dict_to_pydantic_basemodel.src.models.event_page import EventPage
from typed_dict_to_pydantic_basemodel.src.models.event import Event
from typed_dict_to_pydantic_basemodel.src.models.resource import Resource
from typed_dict_to_pydantic_basemodel.src.models.run_start import RunStart
from typed_dict_to_pydantic_basemodel.src.models.run_stop import RunStop
from typed_dict_to_pydantic_basemodel.src.models.stream_datum import StreamDatum
from typed_dict_to_pydantic_basemodel.src.models.stream_resource import StreamResource
from os import listdir

import json
from pathlib import Path


SCHEMA_GENERATED_OUT_DIR = Path(
    "typed_dict_to_pydantic_basemodel/schemas/generated_json_schema"
)
SCHEMA_ORIGINAL_IN_DIR = Path(
    "typed_dict_to_pydantic_basemodel/schemas/original_json_schema"
)

(
    datum_page_original_dict,
    datum_original_dict,
    event_descriptor_original_dict,
    event_original_dict,
    event_page_original_dict,
    resource_original_dict,
    run_start_original_dict,
    run_stop_original_dict,
    stream_datum_original_dict,
    stream_resource_original_dict,
) = (
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "datum_page.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "datum.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "event_descriptor.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "event.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "event_page.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "resource.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "run_start.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "run_stop.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "stream_datum.json").open()),
    json.load(Path(SCHEMA_ORIGINAL_IN_DIR / "stream_resource.json").open()),
)

(
    datum_page_generated_dict,
    datum_generated_dict,
    event_descriptor_generated_dict,
    event_generated_dict,
    event_page_generated_dict,
    resource_generated_dict,
    run_start_generated_dict,
    run_stop_generated_dict,
    stream_datum_generated_dict,
    stream_resource_generated_dict,
) = (
    export_typedict_to_json_schema(DatumPage, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(Datum, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(EventDescriptor, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(Event, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(EventPage, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(Resource, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(RunStart, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(RunStop, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(StreamDatum, out_dir=SCHEMA_GENERATED_OUT_DIR),
    export_typedict_to_json_schema(StreamResource, out_dir=SCHEMA_GENERATED_OUT_DIR),
)


def elements_in_x_not_equal_to_elements_in_y(x: dict, y: dict, title="", parent=""):

    if not title:
        title = y["title"]

    elements = []
    for key_x in x:

        if key_x not in y:
            elements.append(f"{title} has no field {parent}[{key_x}]")

        elif isinstance(x[key_x], dict):
            elements += elements_in_x_not_equal_to_elements_in_y(
                x[key_x], y[key_x], parent=f"{parent}[{key_x}]", title=title
            )

        else:
            if isinstance(x[key_x], list):
                if set(x[key_x]) != set(y[key_x]):
                    elements.append(
                        f"x{parent}[{key_x}] = {set(x[key_x])}, y[{key_x} = {set(y[key_x])}]"
                    )
            if x[key_x] != y[key_x]:
                elements.append(f"x[{key_x}] = {x[key_x]}, y[{key_x}] = {y[key_x]}]")

    return elements


missing_elements = (
    elements_in_x_not_equal_to_elements_in_y(
        datum_page_original_dict, datum_page_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(datum_original_dict, datum_generated_dict),
    elements_in_x_not_equal_to_elements_in_y(
        event_descriptor_original_dict, event_descriptor_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(
        event_page_original_dict, event_page_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(event_original_dict, event_generated_dict),
    elements_in_x_not_equal_to_elements_in_y(
        resource_original_dict, resource_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(
        run_start_original_dict, run_start_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(
        run_stop_original_dict, run_stop_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(
        stream_datum_original_dict, stream_datum_generated_dict
    ),
    elements_in_x_not_equal_to_elements_in_y(
        stream_resource_original_dict, stream_resource_generated_dict
    ),
)

for i in missing_elements:
    if not i:
        continue
    print(f"file {missing_elements.index(i)}")
    for j in i:
        print(f"\t{j}")
