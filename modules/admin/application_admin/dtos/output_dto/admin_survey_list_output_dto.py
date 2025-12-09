from datetime import datetime
from typing import Optional

from pydantic import Field

from common.application import dtos as common_dtos


class AdminSurveyListOutputDTO(common_dtos.BaseDTO):
    id: int = Field(..., description="Unique identifier for the survey")
    survey_type: Optional[str] = Field(
        None, description="Type of the survey (e.g., 'Survey 1', 'Survey 2')"
    )
    visit_date: Optional[datetime] = Field(None, description="Date of the visit")
    state: Optional[str] = Field(None, description="Status of the survey")
    property_city: Optional[str] = Field(None, description="City of the property")
    property_name: Optional[str] = Field(None, description="Name of the property")
    user_producter_name: Optional[str] = Field(
        None, description="Name of the user producer"
    )
    pdf_url: Optional[str] = Field(
        None, description="Public URL for the survey PDF (if available)"
    )
