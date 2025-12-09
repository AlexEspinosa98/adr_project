from common.application.dtos.base_dto import BaseDTO


class LoginUserExtensionistInputDTO(BaseDTO):
    email: str
    password: str
