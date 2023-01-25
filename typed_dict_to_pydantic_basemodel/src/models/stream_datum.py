from typing import Any, Dict, Annotated

from pydantic import BaseModel, Extra, Field


class StreamDatum(BaseModel):
    """Document to reference a quanta of an externally-stored stream of data."""

    class Config:
        extra = Extra.forbid

    datum_kwargs: Annotated[
        Dict[str, Any],
        Field(
            description="Arguments to pass to the Handler to retrieve one quanta of data",
        ),
    ]
    stream_resource: Annotated[
        str,
        Field(description="The UID of the Stream Resource to which this Datum belongs"),
    ]
    uid: Annotated[
        str,
        Field(
            description="Globally unique identifier for this Datum. A suggested formatting being '<stream_resource>/<stream_name>/<block_id>",
        ),
    ]
    stream_name: Annotated[
        str,
        Field(
            description="The name of the stream that this Datum is providing a block of.",
        ),
    ]
    block_idx: Annotated[
        int,
        Field(
            description="The order in the stream of this block of data. This must be contiguous for a given stream.",
        ),
    ]
    event_count: Annotated[
        int, Field(description="The number of events in this datum.")
    ]
    event_offset: Annotated[
        int,
        Field(
            description="The sequence number of the first event in this block. This increasing value allows the presence of gaps.",
        ),
    ]
