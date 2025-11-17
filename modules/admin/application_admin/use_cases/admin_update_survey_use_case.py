from logging import Logger
from typing import Union, Optional, List
from common.infrastructure.logging.config import get_logger
from modules.surveys.application_surveys.services.update_survey_service import (
    UpdateSurveyService,
)
from modules.admin.application_admin.use_cases.log_admin_action import LogAdminAction
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


class AdminUpdateSurveyUseCase:
    def __init__(
        self,
        update_survey_service: UpdateSurveyService,
        log_admin_action: LogAdminAction,
    ):
        self._update_survey_service = update_survey_service
        self._log_admin_action = log_admin_action

    def execute(
        self,
        admin_user_id: int,
        survey_type: int,
        survey_id: int,
        update_dto: Union[
            UpdateSurvey1InputDTO, UpdateSurvey2InputDTO, UpdateSurvey3InputDTO
        ],
        image_paths: Optional[List[str]] = None,
    ):
        _LOGGER.info(
            f"Admin user {admin_user_id} initiating update for survey type {survey_type}, ID {survey_id}"
        )

        # Reuse the existing survey update logic
        updated_survey = self._update_survey_service.update_survey(
            survey_type=survey_type,
            survey_id=survey_id,
            update_dto=update_dto,
            image_paths=image_paths,
        )

        # Log the admin action
        self._log_admin_action.execute(
            admin_user_id=admin_user_id,
            action_id=4,  # Assuming 4 is for 'Edit Survey'
            description=f"Admin user {admin_user_id} edited survey type {survey_type} with ID {survey_id}. State reset to pending.",
        )

        _LOGGER.info(
            f"Admin user {admin_user_id} successfully updated survey {survey_type} with ID {survey_id}."
        )

        return updated_survey
