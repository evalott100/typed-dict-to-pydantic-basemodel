from enum import Enum
from typing import Any, Dict, List, Optional, Annotated, TypedDict
from apischema import schema


class PathSemantics(Enum):
    posix = "posix"
    windows = "windows"


class StreamResource(TypedDict):
    """Document to reference a collection (e.g. file or group of files) of externally-stored data streams"""

    spec: Annotated[
        str,
        schema(
            description="String identifying the format/type of this Stream Resource, used to identify a compatible Handler",
        ),
    ]
    resource_path: Annotated[
        str, schema(description="Filepath or URI for locating this resource")
    ]
    resource_kwargs: Annotated[
        Dict[str, Any],
        schema(
            description="Additional argument to pass to the Handler to read a Stream Resource",
        ),
    ]
    root: Annotated[
        str,
        schema(
            description="Subset of resource_path that is a local detail, not semantic."
        ),
    ]
    path_semantics: Annotated[
        Optional[PathSemantics], schema(description="Rules for joining paths")
    ]
    uid: Annotated[
        str, schema(description="Globally unique identifier for this Stream Resource")
    ]
    run_start: Annotated[
        Optional[str],
        schema(
            description="Globally unique ID to the run_start document this Stream Resource is associated with.",
        ),
    ]
    stream_names: Annotated[
        List[str],
        schema(
            description="List of the stream names this resource provides",
            min_items=1,
            unique=True,
        ),
    ]
