from logging import Logger
from typing import List, Optional

from common.infrastructure.logging.config import get_logger

from modules.admin.application_admin.dtos.output_dto.admin_survey_list_output_dto import AdminSurveyListOutputDTO
from modules.admin.domain_admin.repositories.admin_survey_repository import AdminSurveyRepository


_LOGGER: Logger = get_logger(__name__)


class GetAdminSurveyListUseCase:
    def __init__(self, admin_survey_repository: AdminSurveyRepository) -> None:
        self._admin_survey_repository: AdminSurveyRepository = admin_survey_repository

    def execute(
        self,
        city: Optional[str] = None,
        extensionist_identification: Optional[str] = None,
        extensionist_name: Optional[str] = None,
    ) -> List[AdminSurveyListOutputDTO]:
        _LOGGER.info(f"Fetching admin survey list with filters - City: {city}, Extensionist Identification: {extensionist_identification}, Extensionist Name: {extensionist_name}")

        surveys = self._admin_survey_repository.find_admin_surveys_with_filters(
            city=city,
            extensionist_identification=extensionist_identification,
            extensionist_name=extensionist_name,
        )

        return surveys
