from typing import Any, Dict, Annotated, TypedDict

from apischema import schema


class StreamDatum(TypedDict):
    """Document to reference a quanta of an externally-stored stream of data."""

    datum_kwargs: Annotated[
        Dict[str, Any],
        schema(
            description="Arguments to pass to the Handler to retrieve one quanta of data",
        ),
    ]
    stream_resource: Annotated[
        str,
        schema(
            description="The UID of the Stream Resource to which this Datum belongs"
        ),
    ]
    uid: Annotated[
        str,
        schema(
            description="Globally unique identifier for this Datum. A suggested formatting being '<stream_resource>/<stream_name>/<block_id>",
        ),
    ]
    stream_name: Annotated[
        str,
        schema(
            description="The name of the stream that this Datum is providing a block of.",
        ),
    ]
    block_idx: Annotated[
        int,
        schema(
            description="The order in the stream of this block of data. This must be contiguous for a given stream.",
        ),
    ]
    event_count: Annotated[
        int, schema(description="The number of events in this datum.")
    ]
    event_offset: Annotated[
        int,
        schema(
            description="The sequence number of the first event in this block. This increasing value allows the presence of gaps.",
        ),
    ]
