from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)


class Survey3(BaseModel):
    id: Optional[int] = Field(
        None, gt=0, description="Unique identifier for the entity"
    )
    extensionist_id: Optional[int]
    user_producter_id: Optional[int]
    user_producter: Optional[UserProducter]
    property_id: Optional[int]
    property: Optional[ProductProperty]
    classification_user: Optional[Dict]
    medition_focalization: Optional[Dict]
    objetive_accompaniment: Optional[str]
    development_accompaniment: Optional[str]
    final_diagnosis: Optional[str]
    recommendations_commitments: Optional[str]
    observations_visited: Optional[str]
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
    phono_extra_1: Optional[str]
    state: SurveyStatus = SurveyStatus.PENDING

    # Cierre y despedida
    date_hour_end: Optional[datetime] = None
    socialization_events_group: Optional[str] = None
    not_agend_new_visit: Optional[str] = None

    # Datos de acompañamiento
    date_acompanamiento: Optional[str] = None
    hour_acompanamiento: Optional[str] = None
    origen_register: Optional[str] = None
    name_acompanamiento: Optional[str] = None

    # Información complementaria
    visit_date: Optional[datetime] = None
    attended_by: Optional[str] = None

    class Config:
        from_attributes = True
        orm_mode = True
