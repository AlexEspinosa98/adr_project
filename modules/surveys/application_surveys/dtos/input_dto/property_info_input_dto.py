from pydantic import BaseModel, field_validator
from typing import Optional
from modules.surveys.application_surveys.utils.property_name_utils import (
    normalize_property_name,
)


class PropertyInfoInputDTO(BaseModel):
    name: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    asnm: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    village: Optional[str] = None
    linea_productive_primary: Optional[str] = None
    linea_productive_secondary: Optional[str] = None
    area_in_production: Optional[str] = None

    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        normalized = normalize_property_name(value)
        if not normalized:
            raise ValueError("Property name cannot be empty")
        return normalized
