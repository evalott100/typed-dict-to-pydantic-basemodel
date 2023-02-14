from typing import Any, Dict, Annotated, TypedDict, List

from pydantic import Field


class StreamDatum(TypedDict):
    """Document to reference a quanta of an externally-stored stream of data."""

    data_keys: Annotated[
        List[str], Field(description="List of keys pointed to in Descriptor.")
    ]
    seq_nums: Annotated[
        Dict[str, int],
        Field(
            description="A slice object showing the Event numbers this StreamDatum corresponds to"
        ),
    ]
    indices: Annotated[
        Dict[str, int],
        Field(
            description="A slice object passed to the StreamResource handler so it can hand back data and timestamps"
        ),
    ]
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
