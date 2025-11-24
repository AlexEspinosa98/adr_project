from logging import Logger
from typing import Any, Dict, Optional, Union
from common.infrastructure.logging.config import get_logger
from modules.surveys.application_surveys.use_cases.update_survey_use_case import (
    UpdateSurveyUseCase,
)
from modules.surveys.application_surveys.dtos.input_dto.update_survey1_input_dto import (
    UpdateSurvey1InputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.update_survey2_input_dto import (
    UpdateSurvey2InputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.update_survey3_input_dto import (
    UpdateSurvey3InputDTO,
)
from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)

_LOGGER: Logger = get_logger(__name__)


class UpdateSurveyService:
    def __init__(self, update_survey_use_case: UpdateSurveyUseCase):
        self._update_survey_use_case = update_survey_use_case

    def update_survey(
        self,
        survey_type: int,
        survey_id: int,
        update_dto: Union[
            UpdateSurvey1InputDTO, UpdateSurvey2InputDTO, UpdateSurvey3InputDTO
        ],
        photo_paths: Optional[SurveyPhotoPathsDTO] = None,
        user_producter_data: Optional[Dict[str, Any]] = None,
        property_data: Optional[Dict[str, Any]] = None,
    ):
        _LOGGER.info(
            f"Service call to update survey type {survey_type}, ID {survey_id}"
        )
        return self._update_survey_use_case.execute(
            survey_type,
            survey_id,
            update_dto,
            photo_paths,
            user_producter_data,
            property_data        
            )
