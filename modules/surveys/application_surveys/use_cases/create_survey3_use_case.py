from logging import Logger
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from modules.surveys.domain_surveys.repositories.survey3_repository import Survey3Repository
from modules.surveys.domain_surveys.repositories.user_producter_repository import UserProducterRepository
from modules.surveys.domain_surveys.repositories.product_property_repository import ProductPropertyRepository
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import ProductProperty
from modules.surveys.domain_surveys.entities.classification_user_entity import ClassificationUser
from modules.surveys.application_surveys.dtos.input_dto.create_survey3_input_dto import CreateSurvey3InputDTO
from modules.surveys.application_surveys.dtos.input_dto.survey_user_producter import SurveyUserProducterInputDTO
from modules.surveys.application_surveys.dtos.input_dto.property_info_input_dto import PropertyInfoInputDTO
from modules.surveys.domain_surveys.repositories.classification_user_repository import ClassificationUserRepository
from modules.surveys.application_surveys.dtos.input_dto.classification_user_input_dto import ClassificationUserInputDTO
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class CreateSurvey3UseCase:
    def __init__(self, survey_repository: Survey3Repository, auth_repository: AuthRepository, user_producter_repository: UserProducterRepository, product_property_repository: ProductPropertyRepository, classification_user_repository: ClassificationUserRepository):
        self._survey_repository = survey_repository
        self._auth_repository = auth_repository
        self._user_producter_repository = user_producter_repository
        self._product_property_repository = product_property_repository
        self._classification_user_repository = classification_user_repository

    def execute(self, input_dto: CreateSurvey3InputDTO, producter_input_dto: SurveyUserProducterInputDTO, property_info_input_dto: PropertyInfoInputDTO, classification_user_input_dto: ClassificationUserInputDTO, api_key: str, image_paths: list[str]) -> Survey3:
        _LOGGER.info(f"Creating new survey 3")

        extensionist = self._auth_repository.get_user_by_api_key(api_key)
        if not extensionist:
            raise Exception("Extensionist not found")

        producter = self._user_producter_repository.get_by_identification(producter_input_dto.identification)
        if not producter:
            producter_entity = UserProducter(**producter_input_dto.dict())
            producter = self._user_producter_repository.save(producter_entity)
            _LOGGER.info(f"Created new UserProducter with ID: {producter.id}")

        property_info = self._product_property_repository.get_by_name(property_info_input_dto.name)
        if not property_info:
            property_entity = ProductProperty(**property_info_input_dto.dict(), user_producter_id=producter.id)
            property_info = self._product_property_repository.save(property_entity)
            _LOGGER.info(f"Created new PropertyInfo with ID: {property_info.id}")

        # Save ClassificationUser

        survey_entity = Survey3(
            extensionist_id=extensionist.id,
            user_producter_id=producter.id,
            property_id=property_info.id,
            classification_user=classification_user_input_dto.dict(), # Use the saved classification user
            medition_focalization=input_dto.medition_focalization,
            objetive_accompaniment=input_dto.objetive_accompaniment,
            initial_diagnosis=input_dto.initial_diagnosis,
            recommendations_commitments=input_dto.recommendations_commitments,
            observations=input_dto.observations,
            visit_date=input_dto.visit_date,
            attended_by=input_dto.attended_by,
            user=input_dto.user,
            worker_up=input_dto.worker_up,
            Household_size=input_dto.Household_size,
            other=input_dto.other,
            photo_user=image_paths[0] if len(image_paths) > 0 else None,
            photo_interaction=image_paths[1] if len(image_paths) > 1 else None,
            photo_panorama=image_paths[2] if len(image_paths) > 2 else None,
            phono_extra_1=image_paths[3] if len(image_paths) > 3 else None,
            state=input_dto.state
        )

        saved_survey = self._survey_repository.save(survey_entity)
        _LOGGER.info(f"Survey 1 created with ID: {saved_survey.id}")

        # Update ClassificationUser with survey_idd1
        classification_user = ClassificationUser(**classification_user_input_dto.dict())
        classification_user.survey_idd3 = saved_survey.id
        classification_user_saved = self._classification_user_repository.save(classification_user) # Save the updated classification user
        _LOGGER.info(f"Updated ClassificationUser {classification_user_saved.id} with survey_idd1: {saved_survey.id}")

        return saved_survey
