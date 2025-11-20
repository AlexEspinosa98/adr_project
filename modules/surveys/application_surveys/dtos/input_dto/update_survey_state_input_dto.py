from pydantic import BaseModel, validator
from typing import Literal, Optional


class UpdateSurveyStateInputDTO(BaseModel):
    new_state: Literal["accepted", "rejected"]
    rejection_reason: Optional[str] = None

    @validator("rejection_reason")
    def reason_required_for_rejection(cls, v, values):
        if values.get("new_state") == "rejected" and not v:
            raise ValueError("rejection_reason is required when new_state is 'rejected'")
        return v
