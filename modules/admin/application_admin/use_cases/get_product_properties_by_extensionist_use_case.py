from logging import Logger
from typing import List

from common.infrastructure.logging.config import get_logger
from modules.admin.domain_admin.repositories.admin_survey_repository import (
    AdminSurveyRepository,
)
from modules.admin.application_admin.dtos.output_dto.product_property_output_dto import (
    ProductPropertyOutputDTO,
)


_LOGGER: Logger = get_logger(__name__)


class GetProductPropertiesByExtensionistUseCase:
    def __init__(self, admin_survey_repository: AdminSurveyRepository) -> None:
        self._admin_survey_repository: AdminSurveyRepository = admin_survey_repository

    def execute(
        self, extensionist_id: int, property_name: str = None
    ) -> List[ProductPropertyOutputDTO]:
        _LOGGER.info(
            f"Fetching unique product properties for extensionist ID: [{extensionist_id}] with property name filter: [{property_name}]"
        )
        return self._admin_survey_repository.find_product_properties_by_extensionist_id(
            extensionist_id, property_name
        )
