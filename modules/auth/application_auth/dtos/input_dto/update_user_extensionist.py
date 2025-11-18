from typing import Optional
from common.application.dtos.base_dto import BaseDTO


class UpdateUserExtensionistInputDTO(BaseDTO):
    user_id: int
    name: str | None = None
    phone: Optional[str] = None
    city: Optional[str] = None
    zone: Optional[str] = None
    email: Optional[str] = None
