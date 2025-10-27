from typing import Union

from modules.admin.application_admin.dtos.output_dto.admin_survey1_detail_output_dto import AdminSurvey1DetailOutputDTO
from modules.admin.application_admin.dtos.output_dto.admin_survey2_detail_output_dto import AdminSurvey2DetailOutputDTO
from modules.admin.application_admin.dtos.output_dto.admin_survey3_detail_output_dto import AdminSurvey3DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey1_detail_output_dto import Survey1DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey2_detail_output_dto import Survey2DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.survey3_detail_output_dto import Survey3DetailOutputDTO


class AdminSurveyDetailMapper:
    @staticmethod
    def to_admin_survey_detail_output_dto(
        survey_detail_dto: Union[Survey1DetailOutputDTO, Survey2DetailOutputDTO, Survey3DetailOutputDTO]
    ) -> Union[AdminSurvey1DetailOutputDTO, AdminSurvey2DetailOutputDTO, AdminSurvey3DetailOutputDTO]:
        if isinstance(survey_detail_dto, Survey1DetailOutputDTO):
            return AdminSurvey1DetailOutputDTO.model_validate(survey_detail_dto.model_dump())
        elif isinstance(survey_detail_dto, Survey2DetailOutputDTO):
            return AdminSurvey2DetailOutputDTO.model_validate(survey_detail_dto.model_dump())
        elif isinstance(survey_detail_dto, Survey3DetailOutputDTO):
            return AdminSurvey3DetailOutputDTO.model_validate(survey_detail_dto.model_dump())
        else:
            raise ValueError("Unknown survey detail DTO type")
