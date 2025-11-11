from logging import Logger
from typing import Union

from common.infrastructure.logging.config import get_logger

from modules.surveys.application_surveys.services.get_survey_detail_service import GetSurveyDetailService
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import Survey1DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import Survey2DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import Survey3DetailOutputDTO
from modules.admin.application_admin.mappers.admin_survey_detail_mapper import AdminSurveyDetailMapper # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey1_detail_output_dto import AdminSurvey1DetailOutputDTO # New import
from modules.admin.application_admin.dtos.output_dto.admin_survey2_detail_output_dto import AdminSurvey2DetailOutputDTO 
from modules.admin.application_admin.dtos.output_dto.admin_survey3_detail_output_dto import AdminSurvey3DetailOutputDTO
from modules.surveys.domain_surveys.repositories.classification_user_repository import ClassificationUserRepository
from modules.admin.application_admin.dtos.output_dto.admin_survey_detail_wrapper_output_dto import AdminSurveyDetailWrapperOutputDTO


_LOGGER: Logger = get_logger(__name__)


class GetAdminSurveyDetailUseCase:
    def __init__(
        self,
        get_survey_detail_service: GetSurveyDetailService,
        classification_user_repository: ClassificationUserRepository,
    ) -> None:
        self._get_survey_detail_service: GetSurveyDetailService = get_survey_detail_service
        self._classification_user_repository: ClassificationUserRepository = classification_user_repository

    def execute(
        self, survey_id: int, survey_type: int
    ) -> AdminSurveyDetailWrapperOutputDTO:
        _LOGGER.info(f"Fetching admin survey detail for type {survey_type} with ID {survey_id}")

        survey_detail_dto = self._get_survey_detail_service.get_survey_detail(survey_id, survey_type)

        if not survey_detail_dto:
            _LOGGER.warning(f"Survey detail for type {survey_type} with ID {survey_id} not found")
            return None

        admin_survey_detail_dto = AdminSurveyDetailMapper.to_admin_survey_detail_output_dto(survey_detail_dto)

        user_producter = None
        property_info = None
        
        if hasattr(admin_survey_detail_dto, 'user_producter') and admin_survey_detail_dto.user_producter:
            user_producter = admin_survey_detail_dto.user_producter
        elif hasattr(admin_survey_detail_dto, 'producter') and admin_survey_detail_dto.producter:
             user_producter = admin_survey_detail_dto.producter

        if hasattr(admin_survey_detail_dto, 'property') and admin_survey_detail_dto.property:
            property_info = admin_survey_detail_dto.property

        classification_general = self._classification_user_repository.find_by_survey_id(survey_id, survey_type)

        return AdminSurveyDetailWrapperOutputDTO(
            data_survey=admin_survey_detail_dto,
            property=property_info,
            user_producter=user_producter,
            classification_general=classification_general.model_dump() if classification_general else None,
        )
