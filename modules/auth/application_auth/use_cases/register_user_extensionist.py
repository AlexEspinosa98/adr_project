import secrets
from logging import Logger
from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.auth.application_auth.dtos.input_dto.register_user_extensionist import RegisterUserExtensionistInputDTO
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class RegisterUserExtensionistUseCase:
    def __init__(self, auth_repository: AuthRepository):
        self._auth_repository = auth_repository

    def execute(self, input_dto: RegisterUserExtensionistInputDTO) -> UserExtensionist:
        _LOGGER.info(f"Registering new user extensionist with email: {input_dto.email}")

        # Check if user already exists
        if self._auth_repository.get_user_by_email(input_dto.email):
            raise ValueError(f"User with email {input_dto.email} already exists.")
        if self._auth_repository.get_user_by_identification(input_dto.identification):
            raise ValueError(f"User with identification {input_dto.identification} already exists.")

        user_entity = UserExtensionist(
            name=input_dto.name,
            email=input_dto.email,
            phone=input_dto.phone,
            type_id=input_dto.type_id,
            identification=input_dto.identification,
            city=input_dto.city,
            zone=input_dto.zone,
            api_token=secrets.token_hex(32)
        )

        saved_user = self._auth_repository.save_extensionist(user_entity)
        _LOGGER.info(f"User extensionist registered with ID: {saved_user.id}")
        return saved_user
