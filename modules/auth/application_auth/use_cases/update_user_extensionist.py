from logging import Logger
from modules.auth.domain_auth.entities.auth_entities import UserExtensionist
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.auth.application_auth.dtos.input_dto.update_user_extensionist import (
    UpdateUserExtensionistInputDTO,
)
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)


class UpdateUserExtensionistUseCase:
    def __init__(self, auth_repository: AuthRepository):
        self._auth_repository = auth_repository

    def execute(self, input_dto: UpdateUserExtensionistInputDTO) -> UserExtensionist:
        _LOGGER.info(f"Updating user extensionist with ID: {input_dto.user_id}")

        user_entity = self._auth_repository.get_by_id(input_dto.user_id)
        if not user_entity:
            raise ValueError(f"User with ID {input_dto.user_id} not found.")

        if input_dto.name is not None:
            user_entity.name = input_dto.name
        if input_dto.phone is not None:
            user_entity.phone = input_dto.phone
        if input_dto.city is not None:
            user_entity.city = input_dto.city
        if input_dto.zone is not None:
            user_entity.zone = input_dto.zone
        if input_dto.email is not None:
            user_entity.email = input_dto.email

        updated_user = self._auth_repository.save_extensionist(user_entity)
        _LOGGER.info(f"User extensionist with ID {updated_user.id} updated.")
        return updated_user
