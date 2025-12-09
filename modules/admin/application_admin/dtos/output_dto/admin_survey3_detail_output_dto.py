from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import (
    UserProducterOutputDTO,
)
from modules.admin.application_admin.dtos.output_dto.product_property_output_dto import (
    ProductPropertyOutputDTO,
)


class AdminSurvey3DetailOutputDTO(BaseModel):
    id: int
    user_producter: Optional[UserProducterOutputDTO]
    property: Optional[ProductPropertyOutputDTO]
    classification_user: Optional[Dict]
    medition_focalization: Optional[Dict]
    objetive_accompaniment: Optional[Dict]
    initial_diagnosis: Optional[str]
    recommendations_commitments: Optional[str]
    observations_visited: Optional[str]
    visit_date: Optional[datetime]
    attended_by: Optional[str]
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
    phono_extra_1: Optional[str]
    state: Optional[SurveyStatus] = SurveyStatus.PENDING

    class Config:
        from_attributes = True
