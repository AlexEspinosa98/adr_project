from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import UserProducterOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.product_property_output_dto import ProductPropertyOutputDTO

class Survey3DetailOutputDTO(BaseModel):
    id: int
    user_producter: Optional[UserProducterOutputDTO]
    property: Optional[ProductPropertyOutputDTO]
    classification_user: Optional[Dict] # This is excluded from the main request, but it\'s part of Survey3 entity
    medition_focalization: Optional[Dict]
    objetive_accompaniment: Optional[str]
    initial_diagnosis: Optional[str]
    recommendations_commitments: Optional[str]
    observations: Optional[str]
    visit_date: Optional[datetime]
    attended_by: Optional[str]
    user: Optional[str]
    worker_up: Optional[str]
    Household_size: Optional[str]
    other: Optional[str]
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
    phono_extra_1: Optional[str]
    state: Optional[SurveyStatus] = SurveyStatus.PENDING

    class Config:
        from_attributes = True
