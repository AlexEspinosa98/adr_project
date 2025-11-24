from pydantic import BaseModel
from typing import Optional


class SurveyUserProducterInputDTO(BaseModel):
    identification: str
    name: Optional[str] = None
    type_id: Optional[str] = None
    number_phone: Optional[str] = None
    is_woman_rural: Optional[bool] = None
    is_young_rural: Optional[bool] = None
    ethnic_belonging: Optional[bool] = None
    is_victim_conflict: Optional[bool] = None
    is_narp: Optional[bool] = None
    is_producer_organization_member: Optional[bool] = None
    organization_name: Optional[str] = None
    representantive1_name: Optional[str] = None
