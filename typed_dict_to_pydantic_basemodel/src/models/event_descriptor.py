from enum import Enum
from typing import Any, Dict, List, Optional, Annotated

from pydantic import BaseModel, Extra, Field, constr


class Dtype(Enum):
    string = "string"
    number = "number"
    array = "array"
    boolean = "boolean"
    integer = "integer"


class DataKey(BaseModel):
    dtype: Annotated[Dtype, Field(description="The type of the data in the event.")]

    external: Annotated[
        Optional[constr(regex=r"^[A-Z]+:?")],
        Field(
            description="Where the data is stored if it is stored external to the events.",
        ),
    ]
    shape: Annotated[
        List[int],
        Field(description="The shape of the data.  Empty list indicates scalar data."),
    ]
    dims: Annotated[
        Optional[List[str]],
        Field(
            description="The names for dimensions of the data. Null or empty list if scalar data",
        ),
    ]
    source: Annotated[
        str, Field(description="The source (ex piece of hardware) of the data.")
    ]
    object_name: Annotated[
        Optional[str],
        Field(description="The name of the object this key was pulled from."),
    ]


class DataType(BaseModel):
    __root__: Annotated[Any, Field(title="data_type")]


class ObjectHints(BaseModel):
    __root__: Annotated[Any, Field(title="Object Hints")]


class PerObjectHint(BaseModel):
    fields: Annotated[
        Optional[List[str]],
        Field(description="The 'interesting' data keys for this device."),
    ]


class Configuration(BaseModel):
    data: Annotated[
        Optional[Dict[str, Any]], Field(description="The actual measurement data")
    ]
    timestamps: Annotated[
        Optional[Dict[str, Any]],
        Field(description="The timestamps of the individual measurement data"),
    ]
    data_keys: Annotated[
        Optional[Dict[str, DataKey]],
        Field(
            description="This describes the data stored alongside it in this configuration object.",
        ),
    ]


class EventDescriptor(BaseModel):
    """Document to describe the data captured in the associated event documents"""

    class Config:
        extra = Extra.forbid

    data_keys: Annotated[
        Dict[str, DataKey],
        Field(
            description="This describes the data in the Event Documents.",
            title="data_keys",
        ),
    ]
    uid: Annotated[
        str,
        Field(description="Globally unique ID for this event descriptor.", title="uid"),
    ]
    run_start: Annotated[
        str, Field(description="Globally unique ID of this run's 'start' document.")
    ]
    time: Annotated[
        float, Field(description="Creation time of the document as unix epoch time.")
    ]
    hints: Optional[ObjectHints] = None
    object_keys: Annotated[
        Optional[Dict[str, Any]],
        Field(
            description="Maps a Device/Signal name to the names of the entries it produces in data_keys.",
        ),
    ]
    name: Annotated[
        Optional[str],
        Field(
            description="A human-friendly name for this data stream, such as 'primary' or 'baseline'.",
        ),
    ]
    configuration: Annotated[
        Optional[Dict[str, Configuration]],
        Field(
            description="Readings of configurational fields necessary for interpreting data in the Events.",
        ),
    ]
