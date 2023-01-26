from enum import Enum
from typing import Any, Dict, List, Optional, Union, Annotated, TypedDict

from apischema import schema


class Hints(TypedDict):

    dimensions: Annotated[
        Optional[List[List[Union[List[str], str]]]],
        schema(
            description="The independent axes of the experiment.  Ordered slow to fast",
        ),
    ]


class DataType(TypedDict):
    __root__: Annotated[Any, schema(title="data_type")]


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
        str, schema(description="callable function to perform calculation")
    ]
    args: Optional[List]
    kwargs: Annotated[
        Optional[Dict[str, Any]], schema(description="kwargs for calcalation callable")
    ]


class Projection(TypedDict):
    type: Annotated[
        Optional[Type],
        schema(
            description="linked: a value linked from the data set, calculated: a value that requires calculation, static:  a value defined here in the projection ",
        ),
    ]
    stream: Optional[str]
    location: Annotated[
        Optional[Location],
        schema(
            description="start comes from metadata fields in the start document, event comes from event, configuration comes from configuration fields in the event_descriptor document",
        ),
    ]
    field: Optional[str]
    config_index: Optional[int]
    config_device: Optional[str]
    calculation: Annotated[
        Optional[Calculation],
        schema(
            description="required fields if type is calculated",
            title="calculation properties",
        ),
    ]
    value: Annotated[
        Optional[Any],
        schema(
            description="value explicitely defined in the projection when type==static.",
        ),
    ]


class Projections(TypedDict):
    name: Annotated[Optional[str], schema(description="The name of the projection")]
    version: Annotated[
        str,
        schema(
            description="The version of the projection spec. Can specify the version of an external specification.",
        ),
    ]
    configuration: Annotated[
        Dict[str, Any], schema(description="Static information about projection")
    ]
    projection: Annotated[Dict[str, Projection], schema(pattern=r".")]


class RunStart(TypedDict):
    """Document created at the start of run.  Provides a seach target and later documents link to it"""

    data_session: Annotated[
        Optional[str],
        schema(
            description="An optional field for grouping runs. The meaning is not mandated, but this is a data management grouping and not a scientific grouping. It is intended to group runs in a visit or set of trials.",
        ),
    ]
    data_groups: Annotated[
        Optional[List[str]],
        schema(
            description="An optional list of data access groups that have meaning to some external system. Examples might include facility, beamline, end stations, proposal, safety form.",
        ),
    ]
    project: Annotated[
        Optional[str], schema(description="Name of project that this run is part of")
    ]
    sample: Annotated[
        Optional[Union[Dict[str, Any], str]],
        schema(
            description="Information about the sample, may be a UID to another collection"
        ),
    ]
    scan_id: Annotated[
        Optional[int], schema(description="Scan ID number, not globally unique")
    ]
    time: Annotated[float, schema(description="Time the run started.  Unix epoch time")]
    uid: Annotated[str, schema(description="Globally unique ID for this run")]
    group: Annotated[
        Optional[str], schema(description="Unix group to associate this data with")
    ]
    owner: Annotated[
        Optional[str], schema(description="Unix owner to associate this data with")
    ]
    projections: Optional[List[Projections]]
    hints: Annotated[Optional[Hints], schema(description="Start-level hints")]
