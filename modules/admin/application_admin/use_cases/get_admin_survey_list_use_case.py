from logging import Logger
from typing import List, Optional

from common.infrastructure.logging.config import get_logger

from modules.admin.application_admin.dtos.output_dto.admin_survey_output_dto import AdminSurveyOutputDTO
from modules.admin.application_admin.mappers.admin_survey_mapper import AdminSurveyMapper
from modules.surveys.domain_surveys.repositories.list_surveys_repository import ListSurveysRepository # Changed import


_LOGGER: Logger = get_logger(__name__)


class GetAdminSurveyListUseCase:
    def __init__(self, survey_repository: ListSurveysRepository) -> None: # Changed type hint
        self._survey_repository: ListSurveysRepository = survey_repository # Changed type hint

    def execute(
        self, city: Optional[str] = None, extensionist: Optional[str] = None
    ) -> List[AdminSurveyOutputDTO]:
        _LOGGER.info(f"Fetching admin survey list with filters - City: {city}, Extensionist: {extensionist}")

        surveys = self._survey_repository.find_admin_surveys_with_filters(
            city=city, extensionist=extensionist
        )

        return [
            AdminSurveyMapper.to_admin_survey_output_dto(
                survey_entity=survey, # Changed parameter name
                extensionist_name=survey.attended_by, 
                city_name=survey.property.city if survey.property else None,
            )
            for survey in surveys
        ]
