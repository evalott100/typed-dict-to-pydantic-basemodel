from typing import Any, Dict, List

from pydantic import BaseModel, Extra, Field


class BulkDatum(BaseModel):
    class Config:
        extra = Extra.forbid

    datum_kwarg_list: List[Dict[str, Any]] = Field(
        ...,
        description="Array of arguments to pass to the Handler to retrieve one quanta of data",
    )
    resource: str = Field(
        ..., description="UID of the Resource to which all these Datum documents belong"
    )
    datum_ids: List[str] = Field(
        ...,
        description="Globally unique identifiers for each Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
    )
