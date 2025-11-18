from common.application.dtos.base_dto import BaseDTO


class UpdateUserExtensionistOutputDTO(BaseDTO):
    name: str
    email: str
    phone: str
    city: str
    zone: str
