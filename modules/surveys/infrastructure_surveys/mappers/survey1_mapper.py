from modules.surveys.domain_surveys.entities.survey1_entity import Survey1 as Survey1Entity
from common.infrastructure.database.models.survey import Survey1 as Survey1Model

class Survey1Mapper:
    @staticmethod
    def to_db_model(survey_entity: Survey1Entity) -> Survey1Model:
        return Survey1Model(
            id=survey_entity.id if survey_entity.id != 0 else None,
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

    @staticmethod
    def to_entity(survey_model: Survey1Model) -> Survey1Entity:
        return Survey1Entity(
            id=survey_model.id,
            extensionist_id=survey_model.extensionist_id,
            producter_id=survey_model.producter_id,
            property_id=survey_model.property_id,
            visit_date=survey_model.visit_date,
            attended_by=survey_model.attended_by,
            attended_role=survey_model.attended_role,
            human_technical_capacities=survey_model.human_technical_capacities,
            social_associativity=survey_model.social_associativity,
            technology_access=survey_model.technology_access,
            natural_resources_management=survey_model.natural_resources_management,
            public_policy_participation=survey_model.public_policy_participation,
            is_woman_rural=survey_model.is_woman_rural,
            is_young_rural=survey_model.is_young_rural,
            ethnic_belonging=survey_model.ethnic_belonging,
            is_narp=survey_model.is_narp,
            is_victim_conflict=survey_model.is_victim_conflict,
            control_resources=survey_model.control_resources,
            control_resources_obs=survey_model.control_resources_obs,
            decision_voice=survey_model.decision_voice,
            decision_voice_obs=survey_model.decision_voice_obs,
            innovation_leadership=survey_model.innovation_leadership,
            innovation_leadership_obs=survey_model.innovation_leadership_obs,
            knowledge_dialogue=survey_model.knowledge_dialogue,
            knowledge_dialogue_obs=survey_model.knowledge_dialogue_obs,
            objective=survey_model.objective,
            initial_diagnosis=survey_model.initial_diagnosis,
            recommendations=survey_model.recommendations,
            observations=survey_model.observations,
            photo_user=survey_model.photo_user,
            photo_interaction=survey_model.photo_interaction,
            photo_panorama=survey_model.photo_panorama
        )
