from pydantic import BaseModel
from typing import Optional, Union, Dict, Any
from .admin_survey1_detail_output_dto import AdminSurvey1DetailOutputDTO
from .admin_survey2_detail_output_dto import AdminSurvey2DetailOutputDTO
from .admin_survey3_detail_output_dto import AdminSurvey3DetailOutputDTO
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import UserProducterOutputDTO
from .product_property_output_dto import ProductPropertyOutputDTO

class AdminSurveyDetailWrapperOutputDTO(BaseModel):
    data_survey: Union[AdminSurvey1DetailOutputDTO, AdminSurvey2DetailOutputDTO, AdminSurvey3DetailOutputDTO]
    property: Optional[ProductPropertyOutputDTO]
    user_producter: Optional[UserProducterOutputDTO]
    classification_general: Optional[Any]
