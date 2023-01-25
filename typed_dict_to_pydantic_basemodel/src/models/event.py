from typing import Any, Dict, Optional, Union, Annotated

from pydantic import BaseModel, Extra, Field


class Event(BaseModel):
    """Document to record a quanta of collected data"""
    class Config:
        extra = Extra.forbid

    data: Annotated[Dict[str, Any] , Field(description="The actual measurement data")]
    timestamps: Annotated[Dict[str, Any] , Field(
        description="The timestamps of the individual measurement data"
    )]
    filled: Annotated[Optional[Dict[str, Union[bool, str]]] , Field(
        description="Mapping each of the keys of externally-stored data to the boolean False, indicating that the data has not been loaded, or to foreign keys (moved here from 'data' when the data was loaded)",
    )]
    descriptor: Annotated[str , Field(
        description="UID of the EventDescriptor to which this Event belongs"
    )]
    seq_num: Annotated[int , Field(
        description="Sequence number to identify the location of this Event in the Event stream",
    )]
    time: Annotated[float , Field(
        description="The event time. This maybe different than the timestamps on each of the data entries.",
    )]
    uid: Annotated[str , Field(description="Globally unique identifier for this Event")]
