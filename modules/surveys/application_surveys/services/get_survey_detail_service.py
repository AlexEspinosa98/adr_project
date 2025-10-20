from typing import Optional, Union
from modules.surveys.application_surveys.use_cases.get_survey_detail_use_case import GetSurveyDetailUseCase
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import Survey1DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import Survey2DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import Survey3DetailOutputDTO
from logging import Logger
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class GetSurveyDetailService:
    def __init__(self, get_survey_detail_use_case: GetSurveyDetailUseCase):
        self._get_survey_detail_use_case = get_survey_detail_use_case

    def get_survey_detail(self, survey_id: int, survey_type: int) -> Optional[Union[Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO]]:
        _LOGGER.info(f"Getting detail for survey type {survey_type} with ID {survey_id}")
        return self._get_survey_detail_use_case.execute(survey_id, survey_type)