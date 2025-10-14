from common.application.dtos.base_dto import BaseDTO

class RegisterUserExtensionistOutputDTO(BaseDTO):
    id: int
    name: str
    email: str
