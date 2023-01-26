from enum import Enum
from typing import Any, Dict, Optional, Annotated, TypedDict

from pydantic import Field


class ExitStatus(Enum):
    success = "success"
    abort = "abort"
    fail = "fail"


class RunStop(TypedDict):
    """Document for the end of a run indicating the success/fail state of the run and the end time"""

    run_start: Annotated[
        str,
        Field(
            description="Reference back to the run_start document that this document is paired with.",
        ),
    ]
    reason: Annotated[
        Optional[str], Field(description="Long-form description of why the run ended")
    ]
    time: Annotated[float, Field(description="The time the run ended. Unix epoch")]
    exit_status: Annotated[
        ExitStatus, Field(description="State of the run when it ended")
    ]
    uid: Annotated[str, Field(description="Globally unique ID for this document")]
    num_events: Annotated[
        Optional[Dict[str, int]], Field(description="Number of Events per named stream")
    ]


class DataType(TypedDict):
    __root__: Annotated[Any, Field(title="data_type")]
