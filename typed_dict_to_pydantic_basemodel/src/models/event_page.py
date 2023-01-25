from typing import Dict, List, Optional, Union, Annotated

from pydantic import BaseModel, Extra, Field


class Dataframe(BaseModel):
    __root__: Optional[Dict[str, List]] = None


class DataframeForFilled(BaseModel):
    __root__: Optional[Dict[str, List[Union[bool, str]]]] = None


class EventPage(BaseModel):
    """Page of documents to record a quanta of collected data"""

    class Config:
        extra = Extra.forbid

    descriptor: Annotated[
        str,
        Field(
            description="The UID of the EventDescriptor to which all of the Events in this page belong",
        ),
    ]
    data: Annotated[Dataframe, Field(description="The actual measurement data")]
    timestamps: Annotated[
        Dataframe,
        Field(description="The timestamps of the individual measurement data"),
    ]
    filled: Annotated[
        Optional[DataframeForFilled],
        Field(
            description="Mapping each of the keys of externally-stored data to an array containing the boolean False, indicating that the data has not been loaded, or to foreign keys (moved here from 'data' when the data was loaded)",
        ),
    ]
    seq_num: Annotated[
        List[int],
        Field(
            description="Array of sequence numbers to identify the location of each Event in the Event stream",
        ),
    ]
    time: Annotated[
        List[float],
        Field(
            description="Array of Event times. This maybe different than the timestamps on each of the data entries",
        ),
    ]
    uid: Annotated[
        List[str],
        Field(description="Array of globally unique identifiers for each Event"),
    ]
