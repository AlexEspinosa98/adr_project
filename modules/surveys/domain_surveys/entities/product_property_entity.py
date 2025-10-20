from typing import Optional
from common.domain import entities as common_entities
from pydantic import Field

class ProductProperty(common_entities.BaseEntity):
    name: Optional[str] = Field(None, description="Product property name")
    latitude: Optional[str] = Field(None, description="latitude property")
    longitude: Optional[str] = Field(None, description="longitude property")
    asnm: Optional[str] = Field(None, description="asnm property")
    total_area: Optional[str] = Field(None, description="total area property")
    state: Optional[str] = Field(None, description="State of property")
    city: Optional[str] = Field(None, description="city of property")
    village: Optional[str] = Field(None, description="village of property")
    area_total_property: Optional[str] = Field(None, description="area total property")
    linea_productive_primary: Optional[str] = Field(None, description="linea productive primary")
    area_total_linea_productive_primary: Optional[str] = Field(None, description="area total linea primary")
    linea_productive_secondary: Optional[str] = Field(None, description="linea productive secondary")
    area_total_linea_productive_secondary: Optional[str] = Field(None, description="area total in secondary linea")
    area_in_production: Optional[str] = Field(None, description="area in production")
