from typing import Dict, List, Optional, Annotated

from pydantic import BaseModel, Extra, Field


class dataframe(BaseModel):
    __root__: Annotated[
        Optional[Dict[str, List]], Field(description="A DataFrame-like object")
    ] = None


class DatumPage(BaseModel):
    """Page of documents to reference a quanta of externally-stored data"""

    class Config:
        extra = Extra.forbid

    resource: Annotated[
        str,
        Field(
            description="The UID of the Resource to which all Datums in the page belong",
        ),
    ]
    datum_kwargs: Annotated[
        dataframe,
        Field(
            description="Array of arguments to pass to the Handler to retrieve one quanta of data",
        ),
    ]
    datum_id: Annotated[
        List[str],
        Field(
            description="Array unique identifiers for each Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
        ),
    ]
