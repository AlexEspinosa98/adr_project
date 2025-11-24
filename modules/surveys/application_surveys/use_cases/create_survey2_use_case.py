from logging import Logger
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.repositories.survey2_repository import (
    Survey2Repository,
)
from modules.surveys.domain_surveys.repositories.user_producter_repository import (
    UserProducterRepository,
)
from modules.surveys.domain_surveys.repositories.product_property_repository import (
    ProductPropertyRepository,
)
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)
from modules.surveys.application_surveys.dtos.input_dto.create_survey2_input_dto import (
    CreateSurvey2InputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.survey_user_producter import (
    SurveyUserProducterInputDTO,
)
from modules.surveys.application_surveys.dtos.input_dto.property_info_input_dto import (
    PropertyInfoInputDTO,
)
from common.infrastructure.logging.config import get_logger
from modules.surveys.application_surveys.dtos.photo_paths_dto import (
    SurveyPhotoPathsDTO,
)

_LOGGER: Logger = get_logger(__name__)


class CreateSurvey2UseCase:
    def __init__(
        self,
        survey_repository: Survey2Repository,
        auth_repository: AuthRepository,
        user_producter_repository: UserProducterRepository,
        product_property_repository: ProductPropertyRepository,
    ):
        self._survey_repository = survey_repository
        self._auth_repository = auth_repository
        self._user_producter_repository = user_producter_repository
        self._product_property_repository = product_property_repository

    def execute(
        self,
        input_dto: CreateSurvey2InputDTO,
        producter_input_dto: SurveyUserProducterInputDTO,
        property_info_input_dto: PropertyInfoInputDTO,
        api_key: str,
        photo_paths: SurveyPhotoPathsDTO,
    ) -> Survey2:
        _LOGGER.info("Creating new survey 2")

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

        survey_entity = Survey2(
            id=None,
            extensionist_id=extensionist.id,
            producter_id=producter.id,
            property_id=property_info.id,
            objective_accompaniment=input_dto.objective_accompaniment,
            visit_development_follow_up_activities=input_dto.visit_development_follow_up_activities,
            previous_visit_recommendations_fulfilled=input_dto.previous_visit_recommendations_fulfilled,
            recommendations_commitments=input_dto.recommendations_commitments,
            observations_visited=input_dto.observations_visited,
            objective=input_dto.objective,
            visit_followup=input_dto.visit_followup,
            fulfilled_previous_recommendations=input_dto.fulfilled_previous_recommendations,
            new_recommendations=input_dto.new_recommendations,
            observations_seg=input_dto.observations_seg,
            register_coinnovation=input_dto.register_coinnovation,
            local_practice_tool_technology_coinnovation_identified=input_dto.local_practice_tool_technology_coinnovation_identified,
            local_coinovation_or_technology_record=input_dto.local_coinovation_or_technology_record,
            name_innovation=input_dto.name_innovation,
            description_innovation=input_dto.description_innovation,
            problem_solution_innovation=input_dto.problem_solution_innovation,
            origin_and_developers=input_dto.origin_and_developers,
            materials_and_resources=input_dto.materials_and_resources,
            process_functioning=input_dto.process_functioning,
            potential_replication=input_dto.potential_replication,
            observations_extensionist=input_dto.observations_extensionist,
            photo_user=photo_paths.photo_user,
            photo_interaction=photo_paths.photo_interaction,
            photo_panorama=photo_paths.photo_panorama,
            phono_extra_1=photo_paths.phono_extra_1,
            date_hour_end=input_dto.date_hour_end,
            socilization_next_event=input_dto.socilization_next_event,
            visit_date=input_dto.visit_date,
            attended_by=input_dto.attended_by,
            state="pending",
            producter=None,
            property=None,
            date_acompanamiento=input_dto.date_acompanamiento,
            hour_acompanamiento=input_dto.hour_acompanamiento,
            origen_register=input_dto.origen_register,
            name_acompanamiento=input_dto.name_acompanamiento,
        )

        saved_survey = self._survey_repository.save(survey_entity)
        _LOGGER.info(f"Survey 2 created with ID: {saved_survey.id}")

        return saved_survey
