from typing import Optional
from common.domain import entities as common_entities
from pydantic import EmailStr, Field

class UserExtensionist(common_entities.BaseEntity):
    name: Optional[str] = Field(None, description="Extensionist name")
    email: Optional[str] = Field(None, description="Extensionist email")
    phone: Optional[str] = Field(None, description="Extensionist phone")
    type_id: Optional[int] = Field(None, description="Extensionist type id")
    identification: Optional[str] = Field(None, description="Extensionist identification")
    city: Optional[str] = Field(None, description="Extensionist city")
    zone: Optional[str] = Field(None, description="Extensionist zone")
    signing_image_path: Optional[str] = Field(None, description="Path to the signing image")
    api_token: Optional[str] = Field(None, description="API token for the user")

class UserProducter(common_entities.BaseEntity):
    name: Optional[str] = Field(None, description="Producter name")
    type_id: Optional[int] = Field(None, description="Producter type id")
    identification: Optional[str] = Field(None, description="Producter identification")
    is_woman_rural: Optional[bool] = Field(None, description="Is woman rural")
    is_young_rural: Optional[bool] = Field(None, description="Is young rural")
    ethnic_belonging: Optional[bool] = Field(None, description="Ethnic belonging")
    is_victim_conflict: Optional[bool] = Field(None, description="Is victim of conflict")
    is_narp: Optional[bool] = Field(None, description="Is NARP")