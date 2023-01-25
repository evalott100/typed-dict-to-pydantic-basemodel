from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field, constr


class Dtype(Enum):
    string = "string"
    number = "number"
    array = "array"
    boolean = "boolean"
    integer = "integer"


class DataKey(BaseModel):
    dtype: Dtype = Field(..., description="The type of the data in the event.")
    external: Optional[constr(regex=r"^[A-Z]+:?")] = Field(
        None,
        description="Where the data is stored if it is stored external to the events.",
    )
    shape: List[int] = Field(
        ..., description="The shape of the data.  Empty list indicates scalar data."
    )
    dims: Optional[List[str]] = Field(
        None,
        description="The names for dimensions of the data. Null or empty list if scalar data",
    )
    source: str = Field(
        ..., description="The source (ex piece of hardware) of the data."
    )
    object_name: Optional[str] = Field(
        None, description="The name of the object this key was pulled from."
    )


class DataType(BaseModel):
    __root__: Any = Field(..., title="data_type")


class ObjectHints(BaseModel):
    __root__: Any = Field(..., title="Object Hints")


class PerObjectHint(BaseModel):
    fields: Optional[List[str]] = Field(
        None, description="The 'interesting' data keys for this device."
    )


class Configuration(BaseModel):
    data: Optional[Dict[str, Any]] = Field(
        None, description="The actual measurement data"
    )
    timestamps: Optional[Dict[str, Any]] = Field(
        None, description="The timestamps of the individual measurement data"
    )
    data_keys: Optional[Dict[str, DataKey]] = Field(
        None,
        description="This describes the data stored alongside it in this configuration object.",
    )


class EventDescriptor(BaseModel):
    class Config:
        extra = Extra.forbid

    data_keys: Dict[str, DataKey] = Field(
        ...,
        description="This describes the data in the Event Documents.",
        title="data_keys",
    )
    uid: str = Field(
        ..., description="Globally unique ID for this event descriptor.", title="uid"
    )
    run_start: str = Field(
        ..., description="Globally unique ID of this run's 'start' document."
    )
    time: float = Field(
        ..., description="Creation time of the document as unix epoch time."
    )
    hints: Optional[ObjectHints] = None
    object_keys: Optional[Dict[str, Any]] = Field(
        None,
        description="Maps a Device/Signal name to the names of the entries it produces in data_keys.",
    )
    name: Optional[str] = Field(
        None,
        description="A human-friendly name for this data stream, such as 'primary' or 'baseline'.",
    )
    configuration: Optional[Dict[str, Configuration]] = Field(
        None,
        description="Readings of configurational fields necessary for interpreting data in the Events.",
    )
