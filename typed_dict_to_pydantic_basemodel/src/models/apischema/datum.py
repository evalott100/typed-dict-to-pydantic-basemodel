from typing import Any, Dict, Annotated, TypedDict

from apischema import schema


class Datum(TypedDict):
    """Document to reference a quanta of externally-stored data"""

    datum_kwargs: Annotated[
        Dict[str, Any],
        schema(
            description="Arguments to pass to the Handler to retrieve one quanta of data",
        ),
    ]
    resource: Annotated[
        str, schema(description="The UID of the Resource to which this Datum belongs")
    ]
    datum_id: Annotated[
        str,
        schema(
            description="Globally unique identifier for this Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
        ),
    ]
