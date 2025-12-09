from logging import Logger
from typing import List, Optional

from common.infrastructure.logging.config import get_logger
from modules.admin.application_admin.dtos.output_dto.extensionist_name_id_phone_output_dto import (
    ExtensionistNameIdPhoneOutputDTO,
)
from modules.admin.application_admin.mappers.extensionist_name_id_phone_mapper import (
    ExtensionistNameIdPhoneMapper,
)
from modules.admin.domain_admin.repositories.extensionist_user_repository import (
    ExtensionistUserRepository,
)

_LOGGER: Logger = get_logger(__name__)


class GetExtensionistNameIdPhoneListUseCase:
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
        phone: Optional[str] = None,
        city: Optional[str] = None,
    ) -> List[ExtensionistNameIdPhoneOutputDTO]:
        _LOGGER.info("Fetching extensionist names, identification, and phones list")

        extensionists = self._extensionist_user_repository.find_all_with_filters(
            name=name,
            identification=identification,
            phone=phone,
            city=city,
        )

        return [
            ExtensionistNameIdPhoneMapper.to_extensionist_name_id_phone_output_dto(
                extensionist
            )
            for extensionist in extensionists
        ]
