from typing import Optional
from common.domain import entities as common_entities
from pydantic import Field


class SurveyRejection(common_entities.BaseEntity):
    survey_id: int = Field(..., description="ID of the rejected survey")
    survey_type: int = Field(..., description="Type of the rejected survey (1, 2, or 3)")
    reason: str = Field(..., description="Reason for rejection")
    admin_user_id: int = Field(..., description="ID of the admin user who rejected the survey")
