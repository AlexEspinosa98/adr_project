from typing import Optional
from common.application.dtos.base_dto import BaseDTO

class UpdateUserExtensionistBodyDTO(BaseDTO):
    name: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    zone: Optional[str] = None
