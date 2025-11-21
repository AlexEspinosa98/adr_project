from pydantic import BaseModel, validator
from typing import Optional, Dict
from datetime import datetime
import json
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import (
    UserProducterOutputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.product_property_output_dto import (
    ProductPropertyOutputDTO,
)


class Survey1DetailOutputDTO(BaseModel):
    id: int
    user_producter: Optional[UserProducterOutputDTO]
    property: Optional[ProductPropertyOutputDTO]
    classification_user: Optional[Dict]
    medition_focalization: Optional[Dict]
    objetive_accompaniment: Optional[str]
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
    copy_documentation_delivered: Optional[str]
    date_hour_end: Optional[datetime]
    date_acompanamiento: Optional[datetime]
    origen_register: Optional[str]
    name_acompanamiento: Optional[str]
    type_acompanamiento: Optional[str]
    other_acompanamiento: Optional[str]
    rejection_reason: Optional[str] = None

    @validator("classification_user", "medition_focalization", pre=True)
    def parse_json_fields(cls, value):
        if isinstance(value, str):
            return json.loads(value)
        return value

    class Config:
        from_attributes = True
