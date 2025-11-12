from logging import Logger
from typing import List

from common.infrastructure.logging.config import get_logger
from modules.admin.domain_admin.repositories.admin_survey_repository import AdminSurveyRepository
from modules.admin.application_admin.dtos.output_dto.property_survey_output_dto import PropertySurveyOutputDTO


_LOGGER: Logger = get_logger(__name__)


class GetSurveysByPropertyIdUseCase:
    def __init__(self, admin_survey_repository: AdminSurveyRepository) -> None:
        self._admin_survey_repository: AdminSurveyRepository = admin_survey_repository

    def execute(self, property_id: int) -> List[PropertySurveyOutputDTO]:
        _LOGGER.info(f"Fetching surveys for property ID: [{property_id}]")
        return self._admin_survey_repository.find_surveys_by_property_id(property_id)
