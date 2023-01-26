from enum import Enum
from typing import Any, Dict, List, Optional, Union, Annotated, TypedDict

from pydantic import Field, constr


class Hints(TypedDict):
    dimensions: Annotated[
        Optional[List[List[Union[List[str], str]]]],
        Field(
            description="The independent axes of the experiment.  Ordered slow to fast",
        ),
    ]


class DataType(TypedDict):
    __root__: Annotated[Any, Field(title="data_type")]


class Type(Enum):
    linked = "linked"
    calculated = "calculated"
    static = "static"


class Location(Enum):
    start = "start"
    event = "event"
    configuration = "configuration"


class Calculation(TypedDict):
    callable: Annotated[
        str, Field(description="callable function to perform calculation")
    ]
    args: Optional[List]
    kwargs: Annotated[
        Optional[Dict[str, Any]], Field(description="kwargs for calcalation callable")
    ]


class Projection(TypedDict):
    type: Annotated[
        Optional[Type],
        Field(
            description="linked: a value linked from the data set, calculated: a value that requires calculation, static:  a value defined here in the projection ",
        ),
    ]
    stream: Optional[str]
    location: Annotated[
        Optional[Location],
        Field(
            description="start comes from metadata fields in the start document, event comes from event, configuration comes from configuration fields in the event_descriptor document",
        ),
    ]
    field: Optional[str]
    config_index: Optional[int]
    config_device: Optional[str]
    calculation: Annotated[
        Optional[Calculation],
        Field(
            description="required fields if type is calculated",
            title="calculation properties",
        ),
    ]
    value: Annotated[
        Optional[Any],
        Field(
            description="value explicitely defined in the projection when type==static.",
        ),
    ]


class Projections(TypedDict):
    name: Annotated[Optional[str], Field(description="The name of the projection")]
    version: Annotated[
        str,
        Field(
            description="The version of the projection spec. Can specify the version of an external specification.",
        ),
    ]
    configuration: Annotated[
        Dict[str, Any], Field(description="Static information about projection")
    ]
    projection: Dict[constr(regex=r"."), Projection]


class RunStart(TypedDict):
    """Document created at the start of run.  Provides a seach target and later documents link to it"""

    data_session: Annotated[
        Optional[str],
        Field(
            description="An optional field for grouping runs. The meaning is not mandated, but this is a data management grouping and not a scientific grouping. It is intended to group runs in a visit or set of trials.",
        ),
    ]
    data_groups: Annotated[
        Optional[List[str]],
        Field(
            description="An optional list of data access groups that have meaning to some external system. Examples might include facility, beamline, end stations, proposal, safety form.",
        ),
    ]
    project: Annotated[
        Optional[str], Field(description="Name of project that this run is part of")
    ]
    sample: Annotated[
        Optional[Union[Dict[str, Any], str]],
        Field(
            description="Information about the sample, may be a UID to another collection"
        ),
    ]
    scan_id: Annotated[
        Optional[int], Field(description="Scan ID number, not globally unique")
    ]
    time: Annotated[float, Field(description="Time the run started.  Unix epoch time")]
    uid: Annotated[str, Field(description="Globally unique ID for this run")]
    group: Annotated[
        Optional[str], Field(description="Unix group to associate this data with")
    ]
    owner: Annotated[
        Optional[str], Field(description="Unix owner to associate this data with")
    ]
    projections: Optional[List[Projections]]
    hints: Annotated[Optional[Hints], Field(description="Start-level hints")]
