from typing import Dict, List, Optional, Annotated, TypedDict
from apischema import schema


class dataframe(TypedDict):
    __root__: Annotated[
        Optional[Dict[str, List]], schema(description="A DataFrame-like object")
    ]


class DatumPage(TypedDict):
    """Page of documents to reference a quanta of externally-stored data"""

    resource: Annotated[
        str,
        schema(
            description="The UID of the Resource to which all Datums in the page belong",
        ),
    ]
    datum_kwargs: Annotated[
        dataframe,
        schema(
            description="Array of arguments to pass to the Handler to retrieve one quanta of data",
        ),
    ]
    datum_id: Annotated[
        List[str],
        schema(
            description="Array unique identifiers for each Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
        ),
    ]
