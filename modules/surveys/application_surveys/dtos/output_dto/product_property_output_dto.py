from pydantic import BaseModel, Field
from typing import Optional


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

    class Config:
        from_attributes = True
