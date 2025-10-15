from logging import Logger
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.repositories.survey1_repository import Survey1Repository
from modules.surveys.application_surveys.dtos.input_dto.create_survey1 import CreateSurvey1InputDTO
from common.infrastructure.logging.config import get_logger

_LOGGER: Logger = get_logger(__name__)

class CreateSurvey1UseCase:
    def __init__(self, survey_repository: Survey1Repository):
        self._survey_repository = survey_repository

    def execute(self, input_dto: CreateSurvey1InputDTO) -> Survey1:
        _LOGGER.info(f"Creating new survey 1")

        survey_entity = Survey1(
            id=0, # ID will be set by the database
            extensionist_id=input_dto.extensionist_id,
            producter_id=input_dto.producter_id,
            property_id=input_dto.property_id,
            visit_date=input_dto.visit_date,
            attended_by=input_dto.attended_by,
            attended_role=input_dto.attended_role,
            human_technical_capacities=input_dto.human_technical_capacities,
            social_associativity=input_dto.social_associativity,
            technology_access=input_dto.technology_access,
            natural_resources_management=input_dto.natural_resources_management,
            public_policy_participation=input_dto.public_policy_participation,
            is_woman_rural=input_dto.is_woman_rural,
            is_young_rural=input_dto.is_young_rural,
            ethnic_belonging=input_dto.ethnic_belonging,
            is_narp=input_dto.is_narp,
            is_victim_conflict=input_dto.is_victim_conflict,
            control_resources=input_dto.control_resources,
            control_resources_obs=input_dto.control_resources_obs,
            decision_voice=input_dto.decision_voice,
            decision_voice_obs=input_dto.decision_voice_obs,
            innovation_leadership=input_dto.innovation_leadership,
            innovation_leadership_obs=input_dto.innovation_leadership_obs,
            knowledge_dialogue=input_dto.knowledge_dialogue,
            knowledge_dialogue_obs=input_dto.knowledge_dialogue_obs,
            objective=input_dto.objective,
            initial_diagnosis=input_dto.initial_diagnosis,
            recommendations=input_dto.recommendations,
            observations=input_dto.observations,
            photo_user=input_dto.photo_user,
            photo_interaction=input_dto.photo_interaction,
            photo_panorama=input_dto.photo_panorama
        )

        saved_survey = self._survey_repository.save(survey_entity)
        _LOGGER.info(f"Survey 1 created with ID: {saved_survey.id}")
        return saved_survey
