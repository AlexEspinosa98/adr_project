from pydantic import BaseModel
from typing import Optional

class SurveyUserProducterInputDTO(BaseModel):
    identification: str
    name: Optional[str] = None
    type_id: Optional[int] = None
    is_woman_rural: Optional[bool] = None
    is_young_rural: Optional[bool] = None
    ethnic_belonging: Optional[str] = None
    is_victim_conflict: Optional[bool] = None
    is_narp: Optional[bool] = None
