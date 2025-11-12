from pydantic import BaseModel
from typing import Union
from .admin_survey1_detail_output_dto import AdminSurvey1DetailOutputDTO
from .admin_survey2_detail_output_dto import AdminSurvey2DetailOutputDTO
from .admin_survey3_detail_output_dto import AdminSurvey3DetailOutputDTO


class AdminSurveyDetailWrapperOutputDTO(BaseModel):
    data_survey: Union[
        AdminSurvey1DetailOutputDTO,
        AdminSurvey2DetailOutputDTO,
        AdminSurvey3DetailOutputDTO,
    ]
