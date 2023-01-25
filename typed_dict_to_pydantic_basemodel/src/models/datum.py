from typing import Any, Dict

from pydantic import BaseModel, Extra, Field


class Datum(BaseModel):
    class Config:
        extra = Extra.forbid

    datum_kwargs: Dict[str, Any] = Field(
        ...,
        description="Arguments to pass to the Handler to retrieve one quanta of data",
    )
    resource: str = Field(
        ..., description="The UID of the Resource to which this Datum belongs"
    )
    datum_id: str = Field(
        ...,
        description="Globally unique identifier for this Datum (akin to 'uid' for other Document types), typically formatted as '<resource>/<integer>'",
    )
