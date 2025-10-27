from logging import Logger
from typing import Union

from common.infrastructure.logging.config import get_logger

from modules.surveys.application_surveys.services.get_survey_detail_service import GetSurveyDetailService
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import Survey1DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import Survey2DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import Survey3DetailOutputDTO
from modules.admin.application_admin.mappers.admin_survey_detail_mapper import AdminSurveyDetailMapper # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey1_detail_output_dto import AdminSurvey1DetailOutputDTO # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey2_detail_output_dto import AdminSurvey2DetailOutputDTO # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey3_detail_output_dto import AdminSurvey3DetailOutputDTO # New import


_LOGGER: Logger = get_logger(__name__)


class GetAdminSurveyDetailUseCase:
    def __init__(self, get_survey_detail_service: GetSurveyDetailService) -> None:
        self._get_survey_detail_service: GetSurveyDetailService = get_survey_detail_service

    def execute(
        self, survey_id: int, survey_type: int
    ) -> Union[AdminSurvey1DetailOutputDTO, AdminSurvey2DetailOutputDTO, AdminSurvey3DetailOutputDTO]: # Changed return type
        _LOGGER.info(f"Fetching admin survey detail for type {survey_type} with ID {survey_id}")

        survey_detail = self._get_survey_detail_service.get_survey_detail(survey_id, survey_type)

        if not survey_detail:
            _LOGGER.warning(f"Survey detail for type {survey_type} with ID {survey_id} not found")
            return None

        return AdminSurveyDetailMapper.to_admin_survey_detail_output_dto(survey_detail) # Use mapper
