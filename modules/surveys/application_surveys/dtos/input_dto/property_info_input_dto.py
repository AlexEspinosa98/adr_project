from pydantic import BaseModel
from typing import Optional

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
