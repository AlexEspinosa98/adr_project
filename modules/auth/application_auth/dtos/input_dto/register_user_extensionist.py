from common.application.dtos.base_dto import BaseDTO

class RegisterUserExtensionistInputDTO(BaseDTO):
    name: str
    email: str
    phone: str
    type_id: int
    identification: str
    city: str
    zone: str
