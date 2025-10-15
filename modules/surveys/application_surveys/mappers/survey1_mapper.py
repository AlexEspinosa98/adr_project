from modules.surveys.domain_surveys.entities.survey1_entity import Survey1 as Survey1Entity
from modules.surveys.application_surveys.dtos.output_dto.create_survey1 import CreateSurvey1OutputDTO

class Survey1Mapper:
    @staticmethod
    def to_survey1_dto(survey_entity: Survey1Entity) -> CreateSurvey1OutputDTO:
        return CreateSurvey1OutputDTO(
            id=survey_entity.id,
            extensionist_id=survey_entity.extensionist_id,
            producter_id=survey_entity.producter_id,
            property_id=survey_entity.property_id,
            visit_date=survey_entity.visit_date,
            attended_by=survey_entity.attended_by,
            attended_role=survey_entity.attended_role,
            human_technical_capacities=survey_entity.human_technical_capacities,
            social_associativity=survey_entity.social_associativity,
            technology_access=survey_entity.technology_access,
            natural_resources_management=survey_entity.natural_resources_management,
            public_policy_participation=survey_entity.public_policy_participation,
            is_woman_rural=survey_entity.is_woman_rural,
            is_young_rural=survey_entity.is_young_rural,
            ethnic_belonging=survey_entity.ethnic_belonging,
            is_narp=survey_entity.is_narp,
            is_victim_conflict=survey_entity.is_victim_conflict,
            control_resources=survey_entity.control_resources,
            control_resources_obs=survey_entity.control_resources_obs,
            decision_voice=survey_entity.decision_voice,
            decision_voice_obs=survey_entity.decision_voice_obs,
            innovation_leadership=survey_entity.innovation_leadership,
            innovation_leadership_obs=survey_entity.innovation_leadership_obs,
            knowledge_dialogue=survey_entity.knowledge_dialogue,
            knowledge_dialogue_obs=survey_entity.knowledge_dialogue_obs,
            objective=survey_entity.objective,
            initial_diagnosis=survey_entity.initial_diagnosis,
            recommendations=survey_entity.recommendations,
            observations=survey_entity.observations,
            photo_user=survey_entity.photo_user,
            photo_interaction=survey_entity.photo_interaction,
            photo_panorama=survey_entity.photo_panorama
        )
