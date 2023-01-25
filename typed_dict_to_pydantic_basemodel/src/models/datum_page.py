from typing import Dict, List, Optional

from pydantic import BaseModel, Extra, Field


class Dataframe(BaseModel):
    __root__: Optional[Dict[str, List]] = None


class Datum(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: str = Field(
        ...,
        description="The UID of the Resource to which all Datums in the page belong",
    )
    datum_kwargs: Dataframe = Field(
        ...,
        description="Array of arguments to pass to the Handler to retrieve one quanta of data",
    )
    datum_id: List[str] = Field(
        ...,
        description="Array unique identifiers for each Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
    )
