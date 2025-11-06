from typing import Optional, Union
from modules.surveys.domain_surveys.repositories.survey_detail_repository import SurveyDetailRepository
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import Survey1DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import Survey2DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import Survey3DetailOutputDTO
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import UserProducterOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.product_property_output_dto import ProductPropertyOutputDTO


class GetSurveyDetailUseCase:
    def __init__(self, survey_detail_repository: SurveyDetailRepository):
        self._survey_detail_repository = survey_detail_repository

    def execute(self, survey_id: int, survey_type: int) -> Optional[Union[Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO]]:
        survey_entity = self._survey_detail_repository.get_survey_by_id_and_type(survey_id, survey_type)

        if not survey_entity:
            return None
        
        # Map the entity to the specific SurveyDetailOutputDTO
        if isinstance(survey_entity, Survey1):
            return Survey1DetailOutputDTO(
                id=survey_entity.id,
                user_producter=UserProducterOutputDTO.model_validate(survey_entity.user_producter) if survey_entity.user_producter else None,
                property=ProductPropertyOutputDTO.model_validate(survey_entity.property) if survey_entity.property else None,
                medition_focalization=survey_entity.medition_focalization,
                objetive_accompaniment=survey_entity.objetive_accompaniment,
                initial_diagnosis=survey_entity.initial_diagnosis,
                recommendations_commitments=survey_entity.recommendations_commitments,
                observations_visited=survey_entity.observations_visited,
                visit_date=survey_entity.visit_date,
                attended_by=survey_entity.attended_by,
                user=survey_entity.user,
                worker_up=survey_entity.worker_up,
                Household_size=survey_entity.Household_size,
                other=survey_entity.other,
                photo_user=survey_entity.photo_user,
                photo_interaction=survey_entity.photo_interaction,
                photo_panorama=survey_entity.photo_panorama,
                phono_extra_1=survey_entity.phono_extra_1,
                state=survey_entity.state
            )
        elif isinstance(survey_entity, Survey2):
            return Survey2DetailOutputDTO(
                id=survey_entity.id,
                producter=(UserProducterOutputDTO.model_validate(survey_entity.producter)
                           if survey_entity.producter else None),
                property=(ProductPropertyOutputDTO.model_validate(survey_entity.property)
                          if survey_entity.property else None),
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
                state=survey_entity.state
            )
        elif isinstance(survey_entity, Survey3):
            return Survey3DetailOutputDTO(
                id=survey_entity.id,
                user_producter=UserProducterOutputDTO.model_validate(survey_entity.user_producter) if survey_entity.user_producter else None,
                property=ProductPropertyOutputDTO.model_validate(survey_entity.property) if survey_entity.property else None,
                medition_focalization=survey_entity.medition_focalization,
                objetive_accompaniment=survey_entity.objetive_accompaniment,
                development_accompaniment=survey_entity.development_accompaniment,
                final_diagnosis=survey_entity.final_diagnosis,
                recommendations_commitments=survey_entity.recommendations_commitments,
                observations_visited=survey_entity.observations_visited,
                visit_date=survey_entity.visit_date,
                attended_by=survey_entity.attended_by,
                user=survey_entity.user,
                worker_up=survey_entity.worker_up,
                Household_size=survey_entity.Household_size,
                other=survey_entity.other,
                photo_user=survey_entity.photo_user,
                photo_interaction=survey_entity.photo_interaction,
                photo_panorama=survey_entity.photo_panorama,
                phono_extra_1=survey_entity.phono_extra_1,
                state=survey_entity.state
            )
        else:
            return None