from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, Extra, Field


class Event(BaseModel):
    class Config:
        extra = Extra.forbid

    data: Dict[str, Any] = Field(..., description="The actual measurement data")
    timestamps: Dict[str, Any] = Field(
        ..., description="The timestamps of the individual measurement data"
    )
    filled: Optional[Dict[str, Union[bool, str]]] = Field(
        None,
        description="Mapping each of the keys of externally-stored data to the boolean False, indicating that the data has not been loaded, or to foreign keys (moved here from 'data' when the data was loaded)",
    )
    descriptor: str = Field(
        ..., description="UID of the EventDescriptor to which this Event belongs"
    )
    seq_num: int = Field(
        ...,
        description="Sequence number to identify the location of this Event in the Event stream",
    )
    time: float = Field(
        ...,
        description="The event time. This maybe different than the timestamps on each of the data entries.",
    )
    uid: str = Field(..., description="Globally unique identifier for this Event")
