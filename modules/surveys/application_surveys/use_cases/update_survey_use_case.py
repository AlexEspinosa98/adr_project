from logging import Logger
from typing import Union, Optional, List
from common.infrastructure.logging.config import get_logger
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.domain_surveys.repositories.survey1_repository import (
    Survey1Repository,
)
from modules.surveys.domain_surveys.repositories.survey2_repository import (
    Survey2Repository,
)
from modules.surveys.domain_surveys.repositories.survey3_repository import (
    Survey3Repository,
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

_LOGGER: Logger = get_logger(__name__)


class UpdateSurveyUseCase:
    def __init__(
        self,
        survey1_repository: Survey1Repository,
        survey2_repository: Survey2Repository,
        survey3_repository: Survey3Repository,
    ):
        self._repositories = {
            1: survey1_repository,
            2: survey2_repository,
            3: survey3_repository,
        }

    def execute(
        self,
        survey_type: int,
        survey_id: int,
        update_dto: Union[
            UpdateSurvey1InputDTO, UpdateSurvey2InputDTO, UpdateSurvey3InputDTO
        ],
        image_paths: Optional[List[str]] = None,
    ):
        _LOGGER.info(f"Executing update for survey type {survey_type}, ID {survey_id}")

        repository = self._repositories.get(survey_type)
        if not repository:
            raise ValueError("Invalid survey type")

        survey = repository.get_by_id(survey_id)
        if not survey:
            raise ValueError("Survey not found")

        if survey.state != SurveyStatus.REJECTED:
            raise PermissionError(
                f"Survey can only be edited if its state is 'rejected'. Current state is '{survey.state.value}'."
            )

        update_data = update_dto.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if hasattr(survey, field):
                setattr(survey, field, value)

        if image_paths:
            if len(image_paths) > 0:
                survey.photo_user = image_paths[0]
            if len(image_paths) > 1:
                survey.photo_interaction = image_paths[1]
            if len(image_paths) > 2:
                survey.photo_panorama = image_paths[2]
            if len(image_paths) > 3:
                survey.phono_extra_1 = image_paths[3]
        
        # After updating, set the state back to PENDING
        survey.state = SurveyStatus.PENDING

        updated_survey = repository.save(survey)
        _LOGGER.info(f"Survey {survey_type} with ID {survey_id} updated successfully.")

        return updated_survey
