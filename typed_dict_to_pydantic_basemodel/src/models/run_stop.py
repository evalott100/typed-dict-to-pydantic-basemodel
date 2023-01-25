from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Extra, Field


class ExitStatus(Enum):
    success = "success"
    abort = "abort"
    fail = "fail"


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    run_start: str = Field(
        ...,
        description="Reference back to the run_start document that this document is paired with.",
    )
    reason: Optional[str] = Field(
        None, description="Long-form description of why the run ended"
    )
    time: float = Field(..., description="The time the run ended. Unix epoch")
    exit_status: ExitStatus = Field(..., description="State of the run when it ended")
    uid: str = Field(..., description="Globally unique ID for this document")
    num_events: Optional[Dict[str, int]] = Field(
        None, description="Number of Events per named stream"
    )


class DataType(BaseModel):
    __root__: Any = Field(..., title="data_type")
