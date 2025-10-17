from typing import Optional
from common.domain import entities as common_entities
from pydantic import Field

class UserProducter(common_entities.BaseEntity):
    name: Optional[str] = Field(None, description="Producter name")
    type_id: Optional[int] = Field(None, description="Producter type id")
    identification: Optional[str] = Field(None, description="Producter identification")
    is_woman_rural: Optional[bool] = Field(None, description="Is woman rural")
    is_young_rural: Optional[bool] = Field(None, description="Is young rural")
    ethnic_belonging: Optional[str] = Field(None, description="Ethnic belonging")
    is_victim_conflict: Optional[bool] = Field(None, description="Is victim of conflict")
    is_narp: Optional[bool] = Field(None, description="Is NARP")
