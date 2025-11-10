from logging import Logger
from typing import List, Optional

from common.infrastructure.logging.config import get_logger
from modules.admin.application_admin.dtos.output_dto.extensionist_output_dto import (
    ExtensionistOutputDTO,
)
from modules.admin.application_admin.mappers.extensionist_mapper import (
    ExtensionistMapper,
)
from modules.admin.domain_admin.repositories.extensionist_user_repository import (
    ExtensionistUserRepository,
)

_LOGGER: Logger = get_logger(__name__)


class GetExtensionistListUseCase:
    def __init__(
        self, extensionist_user_repository: ExtensionistUserRepository
    ) -> None:
        self._extensionist_user_repository: ExtensionistUserRepository = (
            extensionist_user_repository
        )

    def execute(
        self,
        name: Optional[str] = None,
        identification: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> List[ExtensionistOutputDTO]:
        _LOGGER.info("Fetching extensionist list")

        extensionists = self._extensionist_user_repository.find_all_with_filters(
            name=name,
            identification=identification,
            email=email,
            phone=phone,
        )

        return [
            ExtensionistMapper.to_extensionist_output_dto(extensionist)
            for extensionist in extensionists
        ]
