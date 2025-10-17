from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime
from .survey_user_producter import SurveyUserProducterInputDTO
from .property_info_input_dto import PropertyInfoInputDTO
from common.domain.enums.survey_status import SurveyStatus

class CreateSurvey3InputDTO(BaseModel):
    classification_user: Optional[Dict]
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
    state: Optional[SurveyStatus] = SurveyStatus.PENDING
