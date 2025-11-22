from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class UpdateSurvey3InputDTO(BaseModel):
    classification_user: Optional[Dict] = None
    medition_focalization: Optional[Dict] = None

    # Información de acompañamiento
    objetive_accompaniment: Optional[str] = None
    development_accompaniment: Optional[str] = None
    final_diagnosis: Optional[str] = None
    recommendations_commitments: Optional[str] = None
    observations_visited: Optional[str] = None

    # Cierre y despedida
    date_hour_end: Optional[datetime] = None
    socialization_events_group: Optional[str] = None
    not_agend_new_visit: Optional[str] = None

    # Datos de acompañamiento
    date_acompanamiento: Optional[str] = None
    hour_acompanamiento: Optional[str] = None
    origen_register: Optional[str] = None
    name_acompanamiento: Optional[str] = None

    # Información complementaria (si aplica)
    visit_date: Optional[datetime] = None
    attended_by: Optional[str] = None
