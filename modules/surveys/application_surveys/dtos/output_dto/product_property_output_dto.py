from pydantic import BaseModel, Field, field_validator
from typing import Optional
from modules.surveys.application_surveys.utils.property_name_utils import (
    denormalize_property_name,
)


class ProductPropertyOutputDTO(BaseModel):
    id: int
    name: Optional[str] = Field(None, description="Product property name")
    latitude: Optional[str] = Field(None, description="latitude property")
    longitude: Optional[str] = Field(None, description="longitude property")
    asnm: Optional[str] = Field(None, description="asnm property")
    state: Optional[str] = Field(None, description="State of property")
    city: Optional[str] = Field(None, description="city of property")
    village: Optional[str] = Field(None, description="village of property")
    total_area: Optional[str] = Field(None, description="area total property")
    linea_productive_primary: Optional[str] = Field(
        None, description="linea productive primary"
    )
    area_total_linea_productive_primary: Optional[str] = Field(
        None, description="area total linea primary"
    )
    linea_productive_secondary: Optional[str] = Field(
        None, description="linea productive secondary"
    )
    area_total_linea_productive_secondary: Optional[str] = Field(
        None, description="area total in secondary linea"
    )
    area_in_production: Optional[str] = Field(None, description="area in production")

    @field_validator("name", mode="before")
    @classmethod
    def denormalize_name(cls, value: Optional[str]) -> Optional[str]:
        return denormalize_property_name(value)

    class Config:
        from_attributes = True
