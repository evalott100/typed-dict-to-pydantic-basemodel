from enum import Enum
from typing import Any, Dict, List, Optional, Annotated, TypedDict

from apischema import schema


class Dtype(Enum):
    string = "string"
    number = "number"
    array = "array"
    boolean = "boolean"
    integer = "integer"


class DataKey(TypedDict):
    dtype: Annotated[Dtype, schema(description="The type of the data in the event.")]

    external: Annotated[
        Optional[str],
        schema(
            pattern=r"^[A-Z]+:?",
            description="Where the data is stored if it is stored external to the events.",
        ),
    ]
    shape: Annotated[
        List[int],
        schema(description="The shape of the data.  Empty list indicates scalar data."),
    ]
    dims: Annotated[
        Optional[List[str]],
        schema(
            description="The names for dimensions of the data. Null or empty list if scalar data",
        ),
    ]
    source: Annotated[
        str, schema(description="The source (ex piece of hardware) of the data.")
    ]
    object_name: Annotated[
        Optional[str],
        schema(description="The name of the object this key was pulled from."),
    ]


class DataType(TypedDict):
    __root__: Annotated[Any, schema(title="data_type")]


class ObjectHints(TypedDict):
    __root__: Annotated[Any, schema(title="Object Hints")]


class PerObjectHint(TypedDict):
    fields: Annotated[
        Optional[List[str]],
        schema(description="The 'interesting' data keys for this device."),
    ]


class Configuration(TypedDict):
    data: Annotated[
        Optional[Dict[str, Any]], schema(description="The actual measurement data")
    ]
    timestamps: Annotated[
        Optional[Dict[str, Any]],
        schema(description="The timestamps of the individual measurement data"),
    ]
    data_keys: Annotated[
        Optional[Dict[str, DataKey]],
        schema(
            description="This describes the data stored alongside it in this configuration object.",
        ),
    ]


class EventDescriptor(TypedDict):
    """Document to describe the data captured in the associated event documents"""

    data_keys: Annotated[
        Dict[str, DataKey],
        schema(
            description="This describes the data in the Event Documents.",
            title="data_keys",
        ),
    ]
    uid: Annotated[
        str,
        schema(
            description="Globally unique ID for this event descriptor.", title="uid"
        ),
    ]
    run_start: Annotated[
        str, schema(description="Globally unique ID of this run's 'start' document.")
    ]
    time: Annotated[
        float, schema(description="Creation time of the document as unix epoch time.")
    ]
    hints: Optional[ObjectHints]
    object_keys: Annotated[
        Optional[Dict[str, Any]],
        schema(
            description="Maps a Device/Signal name to the names of the entries it produces in data_keys.",
        ),
    ]
    name: Annotated[
        Optional[str],
        schema(
            description="A human-friendly name for this data stream, such as 'primary' or 'baseline'.",
        ),
    ]
    configuration: Annotated[
        Optional[Dict[str, Configuration]],
        schema(
            description="Readings of configurational fields necessary for interpreting data in the Events.",
        ),
    ]
