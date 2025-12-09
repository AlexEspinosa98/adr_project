from logging import Logger
from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.auth.application_auth.dtos.input_dto.login_user_extensionist_input_dto import (
    LoginUserExtensionistInputDTO,
)
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)


class LoginUserExtensionistUseCase:
    def __init__(self, auth_repository: AuthRepository):
        self._auth_repository = auth_repository

    def execute(self, input_dto: LoginUserExtensionistInputDTO) -> UserExtensionist:
        _LOGGER.info(f"Attempting login for user with email: {input_dto.email}")

        user = self._auth_repository.get_user_by_email(email=input_dto.email)

        if not user:
            raise ValueError("Invalid email or password.")

        if user.password != input_dto.password:
            raise ValueError("Invalid email or password.")

        _LOGGER.info(f"User with email {input_dto.email} logged in successfully.")
        return user
