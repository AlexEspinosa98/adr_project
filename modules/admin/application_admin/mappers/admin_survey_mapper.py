from typing import Optional

from modules.admin.application_admin.dtos.output_dto.admin_survey_output_dto import AdminSurveyOutputDTO
from modules.surveys.domain_surveys.entities.survey_entity import Survey # Changed import


class AdminSurveyMapper:
    @staticmethod
    def to_admin_survey_output_dto(
        survey_entity: Survey, # Changed parameter name
        extensionist_name: Optional[str] = None,
        city_name: Optional[str] = None,
    ) -> AdminSurveyOutputDTO:
        return AdminSurveyOutputDTO(
            id=survey_entity.id,
            extensionist_id=survey_entity.extensionist_id,
            name_extensionist=extensionist_name or survey_entity.attended_by, # Prioritize passed name, fallback to attended_by
            user_producter_id=survey_entity.user_producter_id,
            property_id=survey_entity.property_id,
            city=city_name or (survey_entity.property.city if survey_entity.property else None),
            visit_date=survey_entity.visit_date,
            state=survey_entity.state, # state is already a string in combined Survey entity
            objetive_accompaniment=survey_entity.objetive_accompaniment,
            initial_diagnosis=survey_entity.initial_diagnosis,
            recommendations_commitments=survey_entity.recommendations_commitments,
            observations=survey_entity.observations,
            attended_by=survey_entity.attended_by,
            user=survey_entity.user,
            Household_size=survey_entity.Household_size,
            other=survey_entity.other,
        )
