from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class UpdateSurvey1InputDTO(BaseModel):
    # Campos JSON editables
    medition_focalization: Optional[Dict] = None
    classification_user: Optional[Dict] = None

    # Información de acompañamiento
    objetive_accompaniment: Optional[str] = None
    initial_diagnosis: Optional[str] = None
    recommendations_commitments: Optional[str] = None
    observations_visited: Optional[str] = None

    # Cierre y documentación
    date_hour_end: Optional[datetime] = None
    copy_documentation_delivered: Optional[str] = None

    # Datos de acompañamiento
    date_acompanamiento: Optional[str] = None
    hour_acompanamiento: Optional[str] = None
    origen_register: Optional[str] = None
    name_acompanamiento: Optional[str] = None
    type_acompanamiento: Optional[str] = None
    other_acompanamiento: Optional[str] = None

    # Información complementaria (si aplica)
    visit_date: Optional[datetime] = None
    attended_by: Optional[str] = None
