from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field


class PathSemantics(Enum):
    posix = 'posix'
    windows = 'windows'


class StreamResource(BaseModel):
    class Config:
        extra = Extra.forbid

    spec: str = Field(
        ...,
        description='String identifying the format/type of this Stream Resource, used to identify a compatible Handler',
    )
    resource_path: str = Field(
        ..., description='Filepath or URI for locating this resource'
    )
    resource_kwargs: Dict[str, Any] = Field(
        ...,
        description='Additional argument to pass to the Handler to read a Stream Resource',
    )
    root: str = Field(
        ..., description='Subset of resource_path that is a local detail, not semantic.'
    )
    path_semantics: Optional[PathSemantics] = Field(
        None, description='Rules for joining paths'
    )
    uid: str = Field(
        ..., description='Globally unique identifier for this Stream Resource'
    )
    run_start: Optional[str] = Field(
        None,
        description='Globally unique ID to the run_start document this Stream Resource is associated with.',
    )
    stream_names: List[str] = Field(
        ...,
        description='List of the stream names this resource provides',
        min_items=1,
        unique_items=True,
    )
