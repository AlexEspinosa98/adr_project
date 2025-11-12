from logging import Logger
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.repositories.survey1_repository import (
    Survey1Repository,
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
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)
from modules.surveys.domain_surveys.entities.classification_user_entity import (
    ClassificationUser,
)
from modules.surveys.application_surveys.dtos.input_dto.create_survey1_input_dto import (
    CreateSurvey1InputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.survey_user_producter import (
    SurveyUserProducterInputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.property_info_input_dto import (
    PropertyInfoInputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.classification_user_input_dto import (
    ClassificationUserInputDTO,
)
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)


class CreateSurvey1UseCase:
    def __init__(
        self,
        survey_repository: Survey1Repository,
        auth_repository: AuthRepository,
        user_producter_repository: UserProducterRepository,
        product_property_repository: ProductPropertyRepository,
        classification_user_repository: ClassificationUserRepository,
    ):
        self._survey_repository = survey_repository
        self._auth_repository = auth_repository
        self._user_producter_repository = user_producter_repository
        self._product_property_repository = product_property_repository
        self._classification_user_repository = classification_user_repository

    def execute(
        self,
        input_dto: CreateSurvey1InputDTO,
        producter_input_dto: SurveyUserProducterInputDTO,
        property_info_input_dto: PropertyInfoInputDTO,
        classification_user_input_dto: ClassificationUserInputDTO,
        api_key: str,
        image_paths: list[str],
    ) -> Survey1:
        _LOGGER.info("Creating new survey 1")

        extensionist = self._auth_repository.get_user_by_api_key(api_key)
        if not extensionist:
            raise Exception("Extensionist not found")

        producter = self._user_producter_repository.get_by_identification(
            producter_input_dto.identification
        )
        if not producter:
            producter_entity = UserProducter(**producter_input_dto.dict())
            producter = self._user_producter_repository.save(producter_entity)
            _LOGGER.info(f"Created new UserProducter with ID: {producter.id}")

        property_info = self._product_property_repository.get_by_name(
            property_info_input_dto.name
        )
        if not property_info:
            property_entity = ProductProperty(
                **property_info_input_dto.dict(), user_producter_id=producter.id
            )
            property_info = self._product_property_repository.save(property_entity)
            _LOGGER.info(f"Created new PropertyInfo with ID: {property_info.id}")

        survey_entity = Survey1(
            id=None,
            extensionist_id=extensionist.id,
            user_producter_id=producter.id,
            property_id=property_info.id,
            medition_focalization=input_dto.medition_focalization,
            classification_user=input_dto.classification_user,
            objetive_accompaniment=input_dto.objetive_accompaniment,
            initial_diagnosis=input_dto.initial_diagnosis,
            recommendations_commitments=input_dto.recommendations_commitments,
            observations_visited=input_dto.observations_visited,
            date_acompanamiento=input_dto.date_acompanamiento,
            hour_acompanamiento=input_dto.hour_acompanamiento,
            origen_register=input_dto.origen_register,
            name_acompanamiento=input_dto.name_acompanamiento,
            type_acompanamiento=input_dto.type_acompanamiento,
            other_acompanamiento=input_dto.other_acompanamiento,
            photo_user=image_paths[0] if len(image_paths) > 0 else None,
            photo_interaction=image_paths[1] if len(image_paths) > 1 else None,
            photo_panorama=image_paths[2] if len(image_paths) > 2 else None,
            phono_extra_1=image_paths[3] if len(image_paths) > 3 else None,
            state=input_dto.state,
            date_hour_end=input_dto.date_hour_end,
            copy_documentation_delivered=input_dto.copy_documentation_delivered,
            visit_date=input_dto.visit_date,
            attended_by=input_dto.attended_by,
            user=input_dto.user,
            worker_up=input_dto.worker_up,
            household_size=input_dto.household_size,
            other=input_dto.other,
            user_producter=None,
            property=None,
        )

        saved_survey = self._survey_repository.save(survey_entity)
        _LOGGER.info(f"Survey 1 created with ID: {saved_survey.id}")

        # Update ClassificationUser with survey_idd1
        classification_user = ClassificationUser(**classification_user_input_dto.dict())
        classification_user.survey_idd1 = saved_survey.id
        classification_user_saved = self._classification_user_repository.save(
            classification_user
        )  # Save the updated classification user
        _LOGGER.info(
            f"Updated ClassificationUser {classification_user_saved.id} with survey_idd1: {saved_survey.id}"
        )

        return saved_survey
