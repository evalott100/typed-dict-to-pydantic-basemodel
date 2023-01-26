from typing import Any, Dict, Optional, Union, Annotated, TypedDict

from apischema import schema


class Event(TypedDict):
    """Document to record a quanta of collected data"""

    data: Annotated[Dict[str, Any], schema(description="The actual measurement data")]
    timestamps: Annotated[
        Dict[str, Any],
        schema(description="The timestamps of the individual measurement data"),
    ]
    filled: Annotated[
        Optional[Dict[str, Union[bool, str]]],
        schema(
            description="Mapping each of the keys of externally-stored data to the boolean False, indicating that the data has not been loaded, or to foreign keys (moved here from 'data' when the data was loaded)",
        ),
    ]
    descriptor: Annotated[
        str,
        schema(description="UID of the EventDescriptor to which this Event belongs"),
    ]
    seq_num: Annotated[
        int,
        schema(
            description="Sequence number to identify the location of this Event in the Event stream",
        ),
    ]
    time: Annotated[
        float,
        schema(
            description="The event time. This maybe different than the timestamps on each of the data entries.",
        ),
    ]
    uid: Annotated[str, schema(description="Globally unique identifier for this Event")]
