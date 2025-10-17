from logging import Logger
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.repositories.survey2_repository import Survey2Repository
from modules.auth.domain_auth.repositories.auth_repository import AuthRepository
from modules.auth.domain_auth.entities.auth_entities import UserProducter
from modules.surveys.application_surveys.dtos.input_dto.create_survey2_input_dto import CreateSurvey2InputDTO
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class CreateSurvey2UseCase:
    def __init__(self, survey_repository: Survey2Repository, auth_repository: AuthRepository):
        self._survey_repository = survey_repository
        self._auth_repository = auth_repository

    def execute(self, input_dto: CreateSurvey2InputDTO, api_key: str, image_paths: list[str]) -> Survey2:
        _LOGGER.info(f"Creating new survey 2")

        extensionist = self._auth_repository.get_user_by_api_key(api_key)
        if not extensionist:
            raise Exception("Extensionist not found")

        producter = self._auth_repository.get_user_by_identification(input_dto.producter.identification)
        if not producter:
            producter_entity = UserProducter(**input_dto.producter.dict())
            producter = self._auth_repository.save_producter(producter_entity)
            _LOGGER.info(f"Created new UserProducter with ID: {producter.id}")

        survey_entity = Survey2(
            id=0,
            extensionist_id=extensionist.id,
            producter_id=producter.id,
            property_id=input_dto.property_id,
            objective_accompaniment=input_dto.objective_accompaniment,
            visit_development_follow_up_activities=input_dto.visit_development_follow_up_activities,
            previous_visit_recommendations_fulfilled=input_dto.previous_visit_recommendations_fulfilled,
            recommendations_commitments=input_dto.recommendations_commitments,
            observations=input_dto.observations,
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
            date_hour_end=input_dto.date_hour_end,
            socilization_next_event=input_dto.socilization_next_event,
            copy_documentation_delivered=input_dto.copy_documentation_delivered,
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
        )

        saved_survey = self._survey_repository.save(survey_entity)
        _LOGGER.info(f"Survey 2 created with ID: {saved_survey.id}")
        return saved_survey
