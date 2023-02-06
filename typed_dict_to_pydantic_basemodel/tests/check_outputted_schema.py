from typed_dict_to_pydantic_basemodel.src.typeddict_to_schema import (
    parse_dict_to_pydantic_basemodel,
)

from typed_dict_to_pydantic_basemodel.src.models.pydantic.datum_page import DatumPage
from typed_dict_to_pydantic_basemodel.src.models.pydantic.datum import Datum
from typed_dict_to_pydantic_basemodel.src.models.pydantic.event_descriptor import (
    EventDescriptor,
)
from typed_dict_to_pydantic_basemodel.src.models.pydantic.event_page import EventPage
from typed_dict_to_pydantic_basemodel.src.models.pydantic.event import Event
from typed_dict_to_pydantic_basemodel.src.models.pydantic.resource import Resource
from typed_dict_to_pydantic_basemodel.src.models.pydantic.run_start import RunStart
from typed_dict_to_pydantic_basemodel.src.models.pydantic.run_stop import RunStop
from typed_dict_to_pydantic_basemodel.src.models.pydantic.stream_datum import (
    StreamDatum,
)
from typed_dict_to_pydantic_basemodel.src.models.pydantic.stream_resource import (
    StreamResource,
)
import json
from pathlib import Path


SCHEMA_GENERATED_OUT_DIR = Path(
    "typed_dict_to_pydantic_basemodel/schemas/generated_json_schema"
)
SCHEMA_ORIGINAL_IN_DIR = Path(
    "typed_dict_to_pydantic_basemodel/schemas/original_json_schema"
)

# mypy passes, all values present, and one optional
resource0: Resource = {
    "spec": "spec_val",
    "resource_path": "resource_path_val",
    "resource_kwargs": {},
    "root": "root_val",
    "uid": "uid_val",
    "run_start": "optional_val",
}

# mypy fails, no required "spec" value
resource1: Resource = {
    "resource_path": "resource_path_val",
    "resource_kwargs": {},
    "root": "root_val",
    "uid": "uid_val",
    "run_start": "optional_val",
}

# mpyp fails, foo isn't in the typedict
resource2: Resource = {
    "foo": "bar",
    "spec": "spec_val",
    "resource_path": "resource_path_val",
    "resource_kwargs": {},
    "root": "root_val",
    "uid": "uid_val",
    "run_start": "optional_val",
}

# mpyp fails, resource_kwargs is the wrong type
resource3: Resource = {
    "spec": "spec_val",
    "resource_path": "resource_path_val",
    "resource_kwargs": 5,
    "root": "root_val",
    "uid": "uid_val",
}

original_dicts = (
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

generated_dicts = (
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
    parse_dict_to_pydantic_basemodel(DatumPage, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(Datum, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(EventDescriptor, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(Event, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(EventPage, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(Resource, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(RunStart, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(RunStop, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(StreamDatum, out_dir=SCHEMA_GENERATED_OUT_DIR),
    parse_dict_to_pydantic_basemodel(StreamResource, out_dir=SCHEMA_GENERATED_OUT_DIR),
)


# Silly test to see how well the generated typedicts match the original
def elements_in_x_not_equal_to_elements_in_y(x: dict, y: dict, title="", parent=""):

    if not title:
        title = y["title"]

    elements = []
    for key_x in x:

        if key_x not in y:
            elements.append(f"\t{title} has no field {parent}[{key_x}]")

        elif isinstance(x[key_x], dict):
            elements += elements_in_x_not_equal_to_elements_in_y(
                x[key_x], y[key_x], parent=f"{parent}[{key_x}]", title=title
            )

        else:
            # We don't want to compare order
            if isinstance(y[key_x], list):
                y[key_x] = set(y[key_x])
            if isinstance(x[key_x], list):
                x[key_x] = set(y[key_x])

            if x[key_x] != y[key_x]:
                elements.append(
                    f"\t{title}_original:    {parent}[{key_x}] = {x[key_x]},\n\t{title}_generated:   {parent}[{key_x}] = {y[key_x]}"
                )

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


for (generated, original) in zip(generated_dicts, original_dicts):
    missing_elements = elements_in_x_not_equal_to_elements_in_y(original, generated)
    if not missing_elements:
        continue
    print(generated["title"])
    for missing_element in missing_elements:
        print(missing_element)
