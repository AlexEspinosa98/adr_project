from datetime import datetime
from typing import Optional, Dict
from pydantic import BaseModel, Field

from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)


class Survey(BaseModel):
    id: Optional[int] = Field(
        None, gt=0, description="Unique identifier for the entity"
    )
    survey_type: Optional[str] = Field(
        None, description="Type of the survey (e.g., 'Survey 1', 'Survey 2')"
    )
    extensionist_id: Optional[int] = Field(None, description="ID of the extensionist")
    user_producter_id: Optional[int] = Field(
        None, description="ID of the user producer"
    )
    user_producter: Optional[UserProducter] = Field(None)
    property_id: Optional[int] = Field(None, description="ID of the property")
    property: Optional[ProductProperty] = Field(None)
    objetive_accompaniment: Optional[str] = Field(
        None, description="Objective of accompaniment"
    )
    recommendations_commitments: Optional[str] = Field(
        None, description="Recommendations and commitments"
    )
    observations: Optional[str] = Field(None, description="Observations")
    visit_date: Optional[datetime] = Field(None, description="Date of the visit")
    attended_by: Optional[str] = Field(
        None, description="Person who attended the survey"
    )
    user: Optional[str] = Field(None, description="User associated with the survey")
    household_size: Optional[str] = Field(None, description="Household size")
    other: Optional[str] = Field(None, description="Other information")
    photo_user: Optional[str] = Field(None)
    photo_interaction: Optional[str] = Field(None)
    photo_panorama: Optional[str] = Field(None)
    phono_extra_1: Optional[str] = Field(None)
    state: Optional[str] = Field(None, description="Status of the survey")

    # Fields specific to Survey1/Survey3
    classification_user: Optional[Dict] = Field(None)
    medition_focalization: Optional[Dict] = Field(None)
    initial_diagnosis: Optional[str] = Field(None)

    # Fields specific to Survey2 (only common ones that might be useful for admin list)
    visit_development_follow_up_activities: Optional[str] = Field(None)
    previous_visit_recommendations_fulfilled: Optional[bool] = Field(None)
    objective: Optional[str] = Field(None)
    visit_followup: Optional[str] = Field(None)
    fulfilled_previous_recommendations: Optional[bool] = Field(None)
    new_recommendations: Optional[str] = Field(None)
    observations_seg: Optional[str] = Field(None)
    register_coinnovation: Optional[str] = Field(None)
    local_practice_tool_technology_coinnovation_identified: Optional[bool] = Field(None)
    local_coinovation_or_technology_record: Optional[bool] = Field(None)
    name_innovation: Optional[str] = Field(None)
    description_innovation: Optional[str] = Field(None)
    problem_solution_innovation: Optional[str] = Field(None)
    origin_and_developers: Optional[str] = Field(None)
    materials_and_resources: Optional[str] = Field(None)
    process_functioning: Optional[str] = Field(None)
    potential_replication: Optional[str] = Field(None)
    observations_extensionist: Optional[str] = Field(None)
    date_hour_end: Optional[datetime] = Field(None)
    socilization_next_event: Optional[str] = Field(None)
    copy_documentation_delivered: Optional[bool] = Field(None)

    class Config:
        from_attributes = True
