from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)


class Survey1(BaseModel):
    # Identificadores principales
    id: Optional[int] = Field(
        None, gt=0, description="Unique identifier for the entity"
    )
    extensionist_id: Optional[int] = Field(
        None, description="ID of the extensionist performing the survey"
    )
    user_producter_id: Optional[int] = Field(
        None, description="ID of the surveyed user/producter"
    )
    property_id: Optional[int] = Field(None, description="ID of the related property")

    # Relaciones (objetos completos opcionales)
    user_producter: Optional[UserProducter] = None
    property: Optional[ProductProperty] = None

    # Campos tipo JSON
    classification_user: Optional[Dict] = Field(
        None, description="User classification data (JSONB field)"
    )
    medition_focalization: Optional[Dict] = Field(
        None, description="Measurement and focalization data (JSONB field)"
    )

    # Información general del acompañamiento
    objetive_accompaniment: Optional[str] = Field(
        None, description="Objective of the accompaniment"
    )
    initial_diagnosis: Optional[str] = Field(None, description="Initial diagnosis text")
    recommendations_commitments: Optional[str] = Field(
        None, description="Recommendations and commitments"
    )
    observations_visited: Optional[str] = Field(
        None, description="Observations during visit"
    )

    # Fotografías asociadas
    photo_user: Optional[str] = Field(None, description="Path to user photo")
    photo_interaction: Optional[str] = Field(
        None, description="Path to interaction photo"
    )
    photo_panorama: Optional[str] = Field(None, description="Path to panorama photo")
    phono_extra_1: Optional[str] = Field(None, description="Path to additional photo")

    # Estado de la encuesta
    state: SurveyStatus = Field(
        default=SurveyStatus.PENDING, description="Current status of the survey"
    )

    # Cierre y documentación
    date_hour_end: Optional[datetime] = Field(
        None, description="End date and time of the accompaniment"
    )

    # Fecha, hora y tipo de acompañamiento
    date_acompanamiento: Optional[str] = Field(
        None, description="Date of the accompaniment (string format)"
    )
    hour_acompanamiento: Optional[str] = Field(
        None, description="Hour of the accompaniment"
    )
    origen_register: Optional[str] = Field(None, description="Origin of the record")
    name_acompanamiento: Optional[str] = Field(
        None, description="Name of the accompaniment type or event"
    )

    # Información complementaria
    visit_date: Optional[datetime] = None
    attended_by: Optional[str] = None

    class Config:
        orm_mode = True
