from typing import Optional
from common.application.dtos.base_dto import BaseDTO


class LoginUserExtensionistOutputDTO(BaseDTO):
    id: int
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    type_id: Optional[int]
    identification: Optional[str]
    city: Optional[str]
    zone: Optional[str]
    api_token: Optional[str]
    signing_image_path: Optional[str]
