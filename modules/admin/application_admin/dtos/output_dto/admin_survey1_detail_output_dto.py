from pydantic import BaseModel, field_validator
from typing import Optional, Dict, Any
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import (
    UserProducterOutputDTO,
)
from modules.admin.application_admin.dtos.output_dto.product_property_output_dto import (
    ProductPropertyOutputDTO,
)
import json


class AdminSurvey1DetailOutputDTO(BaseModel):
    id: int

    # Relaciones anidadas
    user_producter: Optional[UserProducterOutputDTO]
    property: Optional[ProductPropertyOutputDTO]

    # Estructuras JSON (diccionarios)
    classification_user: Optional[Dict]
    medition_focalization: Optional[Dict]
    classification_general: Optional[Dict]  # ← Campo adicional en tu JSON

    # Campos de texto
    objetive_accompaniment: Optional[Dict]
    initial_diagnosis: Optional[str]
    recommendations_commitments: Optional[str]
    observations_visited: Optional[str]

    # Fechas
    visit_date: Optional[datetime]
    date_acompanamiento: Optional[datetime]
    date_hour_end: Optional[datetime]

    # Otros datos administrativos
    attended_by: Optional[str]

    # Fotos
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
    phono_extra_1: Optional[str]

    # Acompañamiento adicional
    origen_register: Optional[str]
    name_acompanamiento: Optional[str]

    # Estado y documentación
    state: Optional[SurveyStatus]

    class Config:
        from_attributes = True

    @field_validator("objetive_accompaniment", mode="before")
    @classmethod
    def parse_objetive_accompaniment(cls, value: Any) -> Optional[Dict]:
        """
        Convierte automáticamente a JSON si viene como string.
        Si ya es dict, lo deja igual.
        """
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                # si no se puede parsear, se deja como None o podrías lanzar un error personalizado
                return None
        return value
