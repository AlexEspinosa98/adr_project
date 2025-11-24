from pydantic import BaseModel, Field
from typing import Optional


class UserProducterOutputDTO(BaseModel):
    id: int
    name: Optional[str] = Field(None, description="Producter name")
    type_id: Optional[str] = Field(None, description="Producter type id")
    identification: Optional[str] = Field(None, description="Producter identification")
    number_phone: Optional[str] = Field(None, description="Producter number phone")
    is_woman_rural: Optional[bool] = Field(None, description="Is woman rural")
    is_young_rural: Optional[bool] = Field(None, description="Is young rural")
    ethnic_belonging: Optional[bool] = Field(None, description="Ethnic belonging")
    is_victim_conflict: Optional[bool] = Field(
        None, description="Is victim of conflict"
    )
    is_narp: Optional[bool] = Field(None, description="Is NARP")
    is_producer_organization_member: Optional[bool] = Field(None, description="Is producer organization member")
    organization_name: Optional[str] = Field(None, description="Organization name")
    representantive1_name: Optional[str] = Field(None, description="Representative name")

    class Config:
        from_attributes = True
