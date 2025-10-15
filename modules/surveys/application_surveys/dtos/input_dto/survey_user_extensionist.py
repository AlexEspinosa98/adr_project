from pydantic import BaseModel
from typing import Optional

class SurveyUserExtensionistInputDTO(BaseModel):
    identification: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    type_id: Optional[int] = None
    city: Optional[str] = None
    zone: Optional[str] = None
