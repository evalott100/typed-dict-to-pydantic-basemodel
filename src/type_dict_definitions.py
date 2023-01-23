from typing import TypedDict, Annotated, List, Dict, Any, Type, _TypedDictMeta
from pydantic import Field


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
