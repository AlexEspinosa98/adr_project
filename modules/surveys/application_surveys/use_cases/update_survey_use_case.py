from logging import Logger
from typing import Any, Dict, Optional, Union
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
from modules.surveys.domain_surveys.repositories.user_producter_repository import (
    UserProducterRepository,
)
from modules.surveys.domain_surveys.repositories.product_property_repository import (
    ProductPropertyRepository,
)
from modules.surveys.domain_surveys.repositories.classification_user_repository import (
    ClassificationUserRepository,
)
from modules.surveys.domain_surveys.entities.classification_user_entity import (
    ClassificationUser,
)
from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)

_LOGGER: Logger = get_logger(__name__)


class UpdateSurveyUseCase:
    def __init__(
        self,
        survey1_repository: Survey1Repository,
        survey2_repository: Survey2Repository,
        survey3_repository: Survey3Repository,
        user_producter_repository: UserProducterRepository,
        product_property_repository: ProductPropertyRepository,
    ):
        self._repositories = {
            1: survey1_repository,
            2: survey2_repository,
            3: survey3_repository,
        }
        self._user_producter_repository = user_producter_repository
        self._product_property_repository = product_property_repository

    def execute(
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

        if photo_paths:
            if photo_paths.photo_user:
                survey.photo_user = photo_paths.photo_user
            if photo_paths.photo_interaction:
                survey.photo_interaction = photo_paths.photo_interaction
            if photo_paths.photo_panorama:
                survey.photo_panorama = photo_paths.photo_panorama
            if photo_paths.phono_extra_1:
                survey.phono_extra_1 = photo_paths.phono_extra_1

        if survey_type in [1, 3]:
            self._update_survey_relations(
                survey,
                user_producter_data,
                property_data,
            )
        
        # After updating, set the state back to PENDING
        survey.state = SurveyStatus.PENDING

        updated_survey = repository.save(survey)
        _LOGGER.info(f"Survey {survey_type} with ID {survey_id} updated successfully.")

        return updated_survey

    def _update_survey_relations(
        self,
        survey,
        user_producter_data: Optional[Dict[str, Any]],
        property_data: Optional[Dict[str, Any]],
    ) -> None:
        if user_producter_data and survey.user_producter_id:
            self._update_user_producter(survey.user_producter_id, user_producter_data)
        if property_data and survey.property_id:
            self._update_product_property(survey.property_id, property_data)

    def _update_user_producter(
        self, producter_id: int, update_data: Dict[str, Any]
    ) -> None:
        producter = self._user_producter_repository.get_by_id(producter_id)
        if not producter:
            return

        for field, value in update_data.items():
            if hasattr(producter, field):
                setattr(producter, field, value)

        self._user_producter_repository.save(producter)

    def _update_product_property(
        self, property_id: int, update_data: Dict[str, Any]
    ) -> None:
        property_info = self._product_property_repository.get_by_id(property_id)
        if not property_info:
            return

        for field, value in update_data.items():
            if hasattr(property_info, field):
                setattr(property_info, field, value)

        self._product_property_repository.save(property_info)

    def _update_classification_user(
        self, survey_id: int, survey_type: int, update_data: Dict[str, Any]
    ) -> None:
        classification_user = self._classification_user_repository.find_by_survey_id(
            survey_id, survey_type
        )

        if classification_user is None:
            classification_user = ClassificationUser(**update_data)
            if survey_type == 1:
                classification_user.survey_idd1 = survey_id
            elif survey_type == 3:
                classification_user.survey_idd3 = survey_id
        else:
            for field, value in update_data.items():
                if hasattr(classification_user, field):
                    setattr(classification_user, field, value)

        self._classification_user_repository.save(classification_user)
