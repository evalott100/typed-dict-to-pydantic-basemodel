from typed_dict_to_pydantic_basemodel.export_to_BaseModel import export_json_schema
from typed_dict_to_pydantic_basemodel.page_type_dicts import BulkDatum, BulkEvents
import json
from pathlib import Path


SCHEMA_DIR = Path("typed_dict_to_pydantic_basemodel/schemas")

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


export_json_schema(BulkDatum)
export_json_schema(BulkEvents)
