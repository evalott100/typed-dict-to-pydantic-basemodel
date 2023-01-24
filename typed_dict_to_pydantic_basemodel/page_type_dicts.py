from typing import TypedDict, Annotated, List, Any, Optional, Type
from pydantic import Field, PyObject


def desc(description: str):
    return Field(description=description)


def title(title: str):
    return Field(title=title)


class BulkDatum(TypedDict):
    # The docstring functions as the description field.
    """Document to reference a quanta of externally-stored data"""

    datum_kwarg_list: Annotated[
        List[Any],
        desc(
            "Array of arguments to pass to the Handler to retrieve one quanta of data"
        ),
    ]

    resource: Annotated[
        str,
        desc("UID of the Resource to which all these Datum documents belong"),
    ]

    datum_ids: Annotated[
        List[str],
        desc(
            "Globally unique identifiers for each Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'"
        ),
    ]


class BulkEvents(TypedDict):
    # The docstring functions as the description field.
    """Document to record a quanta of collected data"""
    filled: Annotated[
        Optional[Type[object]],
        desc(
            "Mapping the keys of externally-stored data to a boolean indicating whether that data has yet been loaded"
        ),
    ]

    data: Annotated[Type[object], desc("The actual measument data")]

    timestamps: Annotated[
        Type[object], desc("The timestamps of the individual measument data")
    ]

    descriptor: Annotated[
        str, desc("UID to point back to Descriptor for this event stream")
    ]

    seq_num: Annotated[
        int,
        desc(
            "Sequence number to identify the location of this Event in the Event stream"
        ),
    ]
    time: Annotated[
        int,
        desc(
            "The event time.  This maybe different than the timestamps on each of the data entries"
        ),
    ]
    uid: Annotated[str, desc("Globally unique identifier for this Event")]