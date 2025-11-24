from common.application.dtos.base_dto import BaseDTO


class LoginUserExtensionistInputDTO(BaseDTO):
    phone: str
    identification: str
