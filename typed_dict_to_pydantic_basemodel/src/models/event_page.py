from typing import Dict, List, Optional, Union, Annotated, TypedDict
from apischema import schema


class Dataframe(TypedDict):
    __root__: Optional[Dict[str, List]]


class DataframeForFilled(TypedDict):
    __root__: Optional[Dict[str, List[Union[bool, str]]]]


class EventPage(TypedDict):
    """Page of documents to record a quanta of collected data"""

    descriptor: Annotated[
        str,
        schema(
            description="The UID of the EventDescriptor to which all of the Events in this page belong",
        ),
    ]
    data: Annotated[Dataframe, schema(description="The actual measurement data")]
    timestamps: Annotated[
        Dataframe,
        schema(description="The timestamps of the individual measurement data"),
    ]
    filled: Annotated[
        Optional[DataframeForFilled],
        schema(
            description="Mapping each of the keys of externally-stored data to an array containing the boolean False, indicating that the data has not been loaded, or to foreign keys (moved here from 'data' when the data was loaded)",
        ),
    ]
    seq_num: Annotated[
        List[int],
        schema(
            description="Array of sequence numbers to identify the location of each Event in the Event stream",
        ),
    ]
    time: Annotated[
        List[float],
        schema(
            description="Array of Event times. This maybe different than the timestamps on each of the data entries",
        ),
    ]
    uid: Annotated[
        List[str],
        schema(description="Array of globally unique identifiers for each Event"),
    ]
