from datetime import datetime
from typing import Optional

from pydantic import Field

from common.application import dtos as common_dtos


class AdminSurveyOutputDTO(common_dtos.BaseDTO):
    id: int = Field(..., description="Unique identifier for the survey")
    extensionist_id: Optional[int] = Field(None, description="ID of the extensionist")
    name_extensionist: Optional[str] = Field(None, description="Name of the extensionist")
    user_producter_id: Optional[int] = Field(None, description="ID of the user producer")
    property_id: Optional[int] = Field(None, description="ID of the property")
    city: Optional[str] = Field(None, description="City of the property")
    visit_date: Optional[datetime] = Field(None, description="Date of the visit")
    state: str = Field(..., description="Status of the survey")
    objetive_accompaniment: Optional[str] = Field(None, description="Objective of accompaniment")
    initial_diagnosis: Optional[str] = Field(None, description="Initial diagnosis")
    recommendations_commitments: Optional[str] = Field(None, description="Recommendations and commitments")
    observations: Optional[str] = Field(None, description="Observations")
    attended_by: Optional[str] = Field(None, description="Person who attended the survey")
    user: Optional[str] = Field(None, description="User associated with the survey")
    Household_size: Optional[str] = Field(None, description="Household size")
    other: Optional[str] = Field(None, description="Other information")
