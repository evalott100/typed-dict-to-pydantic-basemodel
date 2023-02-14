from typing import Any, Dict, Annotated, TypedDict

from pydantic import Field


class Datum(TypedDict):
    """Document to reference a quanta of externally-stored data"""

    resource: Annotated[
        str, Field(description="The UID of the Resource to which this Datum belongs")
    ]
    datum_id: Annotated[
        str,
        Field(
            description="Globally unique identifier for this Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
        ),
    ]
