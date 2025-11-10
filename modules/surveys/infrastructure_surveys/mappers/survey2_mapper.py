from modules.surveys.domain_surveys.entities.survey2_entity import Survey2 as Survey2Entity
from common.infrastructure.database.models.survey import Survey2 as Survey2Model
import json
from datetime import datetime

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

class Survey2Mapper:
    @staticmethod
    def to_db_model(survey_entity: Survey2Entity) -> Survey2Model:
        return Survey2Model(
            id=survey_entity.id if survey_entity.id != 0 else None,
            extensionist_id=survey_entity.extensionist_id,
            producter_id=survey_entity.producter_id,
            property_id=survey_entity.property_id,
            objective_accompaniment=survey_entity.objective_accompaniment,
            visit_development_follow_up_activities=survey_entity.visit_development_follow_up_activities,
            previous_visit_recommendations_fulfilled=survey_entity.previous_visit_recommendations_fulfilled,
            recommendations_commitments=survey_entity.recommendations_commitments,
            observations_visited=survey_entity.observations_visited,
            objective=survey_entity.objective,
            visit_followup=survey_entity.visit_followup,
            fulfilled_previous_recommendations=survey_entity.fulfilled_previous_recommendations,
            new_recommendations=survey_entity.new_recommendations,
            observations_seg=survey_entity.observations_seg,
            register_coinnovation=survey_entity.register_coinnovation,
            local_practice_tool_technology_coinnovation_identified=survey_entity.local_practice_tool_technology_coinnovation_identified,
            local_coinovation_or_technology_record=survey_entity.local_coinovation_or_technology_record,
            name_innovation=survey_entity.name_innovation,
            description_innovation=survey_entity.description_innovation,
            problem_solution_innovation=survey_entity.problem_solution_innovation,
            origin_and_developers=survey_entity.origin_and_developers,
            materials_and_resources=survey_entity.materials_and_resources,
            process_functioning=survey_entity.process_functioning,
            potential_replication=survey_entity.potential_replication,
            observations_extensionist=survey_entity.observations_extensionist,
            photo_user=survey_entity.photo_user,
            photo_interaction=survey_entity.photo_interaction,
            photo_panorama=survey_entity.photo_panorama,
            phono_extra_1=survey_entity.phono_extra_1,
            date_hour_end=survey_entity.date_hour_end,
            socilization_next_event=survey_entity.socilization_next_event,
            copy_documentation_delivered=survey_entity.copy_documentation_delivered,
            visit_date=survey_entity.visit_date,
            attended_by=survey_entity.attended_by,
            user=survey_entity.user,
            worker_up=survey_entity.worker_up,
            Household_size=survey_entity.Household_size,
            other=survey_entity.other,
            state=survey_entity.state,
            date_acompanamiento=survey_entity.date_acompanamiento,
            hour_acompanamiento=survey_entity.hour_acompanamiento,
            origen_register=survey_entity.origen_register,
            name_acompanamiento=survey_entity.name_acompanamiento,
            type_acompanamiento=survey_entity.type_acompanamiento,
            other_acompanamiento=survey_entity.other_acompanamiento
        )

    @staticmethod
    def to_entity(survey_model: Survey2Model) -> Survey2Entity:
        return Survey2Entity(
            id=survey_model.id,
            extensionist_id=survey_model.extensionist_id,
            producter_id=survey_model.producter_id,
            property_id=survey_model.property_id,
            objective_accompaniment=survey_model.objective_accompaniment,
            visit_development_follow_up_activities=survey_model.visit_development_follow_up_activities,
            previous_visit_recommendations_fulfilled=survey_model.previous_visit_recommendations_fulfilled,
            recommendations_commitments=survey_model.recommendations_commitments,
            observations_visited=survey_model.observations_visited,
            objective=survey_model.objective,
            visit_followup=survey_model.visit_followup,
            fulfilled_previous_recommendations=survey_model.fulfilled_previous_recommendations,
            new_recommendations=survey_model.new_recommendations,
            observations_seg=survey_model.observations_seg,
            register_coinnovation=survey_model.register_coinnovation,
            local_practice_tool_technology_coinnovation_identified=survey_model.local_practice_tool_technology_coinnovation_identified,
            local_coinovation_or_technology_record=survey_model.local_coinovation_or_technology_record,
            name_innovation=survey_model.name_innovation,
            description_innovation=survey_model.description_innovation,
            problem_solution_innovation=survey_model.problem_solution_innovation,
            origin_and_developers=survey_model.origin_and_developers,
            materials_and_resources=survey_model.materials_and_resources,
            process_functioning=survey_model.process_functioning,
            potential_replication=survey_model.potential_replication,
            observations_extensionist=survey_model.observations_extensionist,
            photo_user=survey_model.photo_user,
            photo_interaction=survey_model.photo_interaction,
            photo_panorama=survey_model.photo_panorama,
            phono_extra_1=survey_model.phono_extra_1,
            date_hour_end=survey_model.date_hour_end,
            socilization_next_event=survey_model.socilization_next_event,
            copy_documentation_delivered=survey_model.copy_documentation_delivered,
            visit_date=survey_model.visit_date,
            attended_by=survey_model.attended_by,
            user=survey_model.user,
            worker_up=survey_model.worker_up,
            Household_size=survey_model.Household_size,
            other=survey_model.other,
            state=survey_model.state,
            producter=survey_model.producter,
            property=survey_model.property,
            date_acompanamiento=survey_model.date_acompanamiento,
            hour_acompanamiento=survey_model.hour_acompanamiento,
            origen_register=survey_model.origen_register,
            name_acompanamiento=survey_model.name_acompanamiento,
            type_acompanamiento=survey_model.type_acompanamiento,
            other_acompanamiento=survey_model.other_acompanamiento
        )
