from typing import Optional, Union
from modules.surveys.domain_surveys.repositories.survey_detail_repository import (
    SurveyDetailRepository,
)
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import (
    Survey1DetailOutputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import (
    Survey2DetailOutputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import (
    Survey3DetailOutputDTO,
)
from modules.surveys.domain_surveys.entities.survey1_entity import Survey1
from modules.surveys.domain_surveys.entities.survey2_entity import Survey2
from modules.surveys.domain_surveys.entities.survey3_entity import Survey3
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import (
    UserProducterOutputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.product_property_output_dto import (
    ProductPropertyOutputDTO,
)
from modules.surveys.domain_surveys.repositories.survey_rejection_repository import SurveyRejectionRepository
from common.domain.enums.survey_status import SurveyStatus
import os
from common.config.common.settings import settings


def _get_full_image_url(image_path: Optional[str]) -> Optional[str]:
    if image_path:
        # Assuming the base URL for static files is /static/
        # And the UPLOAD_DIRECTORY is 'uploads'
        # So, a path like './uploads/IMG_2057.JPG' becomes '/static/IMG_2057.JPG'
        filename = os.path.basename(image_path)
        return f"{settings.backend_url}/static/{filename}"
    return None


class GetSurveyDetailUseCase:
    def __init__(self, survey_detail_repository: SurveyDetailRepository, survey_rejection_repository: SurveyRejectionRepository):
        self._survey_detail_repository = survey_detail_repository
        self._survey_rejection_repository = survey_rejection_repository

    def execute(
        self, survey_id: int, survey_type: int
    ) -> Optional[
        Union[Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO]
    ]:
        survey_entity = self._survey_detail_repository.get_survey_by_id_and_type(
            survey_id, survey_type
        )

        if not survey_entity:
            return None

        rejection_reason = None
        if survey_entity.state == SurveyStatus.REJECTED:
            rejection = self._survey_rejection_repository.get_by_survey_id_and_type(survey_id, survey_type)
            if rejection:
                rejection_reason = rejection.reason

        # Map the entity to the specific SurveyDetailOutputDTO
        if isinstance(survey_entity, Survey1):
            return Survey1DetailOutputDTO(
                id=survey_entity.id,
                user_producter=UserProducterOutputDTO.model_validate(
                    survey_entity.user_producter
                )
                if survey_entity.user_producter
                else None,
                property=ProductPropertyOutputDTO.model_validate(survey_entity.property)
                if survey_entity.property
                else None,
                classification_user=survey_entity.classification_user,
                medition_focalization=survey_entity.medition_focalization,
                objetive_accompaniment=survey_entity.objetive_accompaniment,
                initial_diagnosis=survey_entity.initial_diagnosis,
                recommendations_commitments=survey_entity.recommendations_commitments,
                observations_visited=survey_entity.observations_visited,
                visit_date=survey_entity.visit_date,
                attended_by=survey_entity.attended_by,
                photo_user=_get_full_image_url(survey_entity.photo_user),
                photo_interaction=_get_full_image_url(survey_entity.photo_interaction),
                photo_panorama=_get_full_image_url(survey_entity.photo_panorama),
                phono_extra_1=_get_full_image_url(survey_entity.phono_extra_1),
                state=survey_entity.state,
                date_hour_end=survey_entity.date_hour_end,
                date_acompanamiento=survey_entity.date_acompanamiento,
                hour_acompanamiento=survey_entity.hour_acompanamiento,
                origen_register=survey_entity.origen_register,
                name_acompanamiento=survey_entity.name_acompanamiento,
                rejection_reason=rejection_reason,
            )
        elif isinstance(survey_entity, Survey2):
            return Survey2DetailOutputDTO(
                id=survey_entity.id,
                producter=(
                    UserProducterOutputDTO.model_validate(survey_entity.producter)
                    if survey_entity.producter
                    else None
                ),
                property=(
                    ProductPropertyOutputDTO.model_validate(survey_entity.property)
                    if survey_entity.property
                    else None
                ),
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
                photo_user=_get_full_image_url(survey_entity.photo_user),
                photo_interaction=_get_full_image_url(survey_entity.photo_interaction),
                photo_panorama=_get_full_image_url(survey_entity.photo_panorama),
                phono_extra_1=_get_full_image_url(survey_entity.phono_extra_1),
                date_hour_end=survey_entity.date_hour_end,
                socilization_next_event=survey_entity.socilization_next_event,
                visit_date=survey_entity.visit_date,
                attended_by=survey_entity.attended_by,
                state=survey_entity.state,
                date_acompanamiento=survey_entity.date_acompanamiento,
                hour_acompanamiento=survey_entity.hour_acompanamiento,
                origen_register=survey_entity.origen_register,
                name_acompanamiento=survey_entity.name_acompanamiento,
                rejection_reason=rejection_reason,
            )
        elif isinstance(survey_entity, Survey3):
            return Survey3DetailOutputDTO(
                id=survey_entity.id,
                user_producter=UserProducterOutputDTO.model_validate(
                    survey_entity.user_producter
                )
                if survey_entity.user_producter
                else None,
                property=ProductPropertyOutputDTO.model_validate(survey_entity.property)
                if survey_entity.property
                else None,
                medition_focalization=survey_entity.medition_focalization,
                objetive_accompaniment=survey_entity.objetive_accompaniment,
                development_accompaniment=survey_entity.development_accompaniment,
                final_diagnosis=survey_entity.final_diagnosis,
                recommendations_commitments=survey_entity.recommendations_commitments,
                observations_visited=survey_entity.observations_visited,
                visit_date=survey_entity.visit_date,
                attended_by=survey_entity.attended_by,
                photo_user=_get_full_image_url(survey_entity.photo_user),
                photo_interaction=_get_full_image_url(survey_entity.photo_interaction),
                photo_panorama=_get_full_image_url(survey_entity.photo_panorama),
                phono_extra_1=_get_full_image_url(survey_entity.phono_extra_1),
                state=survey_entity.state,
                rejection_reason=rejection_reason,
            )
        else:
            return None
