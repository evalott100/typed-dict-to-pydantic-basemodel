from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field, constr


class Hints(BaseModel):
    class Config:
        extra = Extra.forbid

    dimensions: Optional[List[List[Union[List[str], str]]]] = Field(
        None,
        description="The independent axes of the experiment.  Ordered slow to fast",
    )


class DataType(BaseModel):
    __root__: Any = Field(..., title="data_type")


class Type(Enum):
    linked = "linked"
    calculated = "calculated"
    static = "static"


class Location(Enum):
    start = "start"
    event = "event"
    configuration = "configuration"


class Calculation(BaseModel):
    callable: str = Field(..., description="callable function to perform calculation")
    args: Optional[List] = None
    kwargs: Optional[Dict[str, Any]] = Field(
        None, description="kwargs for calcalation callable"
    )


class Projection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[Type] = Field(
        None,
        description="linked: a value linked from the data set, calculated: a value that requires calculation, static:  a value defined here in the projection ",
    )
    stream: Optional[str] = None
    location: Optional[Location] = Field(
        None,
        description="start comes from metadata fields in the start document, event comes from event, configuration comes from configuration fields in the event_descriptor document",
    )
    field: Optional[str] = None
    config_index: Optional[int] = None
    config_device: Optional[str] = None
    calculation: Optional[Calculation] = Field(
        None,
        description="required fields if type is calculated",
        title="calculation properties",
    )
    value: Optional[Any] = Field(
        None,
        description="value explicitely defined in the projection when type==static.",
    )


class Projections(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description="The name of the projection")
    version: str = Field(
        ...,
        description="The version of the projection spec. Can specify the version of an external specification.",
    )
    configuration: Dict[str, Any] = Field(
        ..., description="Static information about projection"
    )
    projection: Dict[constr(regex=r"."), Projection]


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    data_session: Optional[str] = Field(
        None,
        description="An optional field for grouping runs. The meaning is not mandated, but this is a data management grouping and not a scientific grouping. It is intended to group runs in a visit or set of trials.",
    )
    data_groups: Optional[List[str]] = Field(
        None,
        description="An optional list of data access groups that have meaning to some external system. Examples might include facility, beamline, end stations, proposal, safety form.",
    )
    project: Optional[str] = Field(
        None, description="Name of project that this run is part of"
    )
    sample: Optional[Union[Dict[str, Any], str]] = Field(
        None,
        description="Information about the sample, may be a UID to another collection",
    )
    scan_id: Optional[int] = Field(
        None, description="Scan ID number, not globally unique"
    )
    time: float = Field(..., description="Time the run started.  Unix epoch time")
    uid: str = Field(..., description="Globally unique ID for this run")
    group: Optional[str] = Field(
        None, description="Unix group to associate this data with"
    )
    owner: Optional[str] = Field(
        None, description="Unix owner to associate this data with"
    )
    projections: Optional[List[Projections]] = None
    hints: Optional[Hints] = Field(None, description="Start-level hints")
