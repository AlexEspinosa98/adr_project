from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus


class SurveyDetailOutputDTO(BaseModel):
    id: int
    extensionist_id: Optional[int]
    user_producter_id: Optional[int]  # This will cover producter_id for Survey2 as well
    property_id: Optional[int]

    # Survey1 and Survey3 specific fields
    medition_focalization: Optional[Dict]

    # Common fields
    objetive_accompaniment: Optional[str]
    initial_diagnosis: Optional[str]
    recommendations_commitments: Optional[str]
    observations: Optional[str]
    visit_date: Optional[datetime]
    attended_by: Optional[str]
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
    phono_extra_1: Optional[str]
    state: Optional[SurveyStatus]

    # Survey2 specific fields
    objective_accompaniment: Optional[str] = Field(
        None, alias="objective_accompaniment"
    )
    visit_development_follow_up_activities: Optional[str] = Field(
        None, alias="visit_development_follow_up_activities"
    )
    previous_visit_recommendations_fulfilled: Optional[bool] = Field(
        None, alias="previous_visit_recommendations_fulfilled"
    )
    objective: Optional[str] = Field(None, alias="objective")
    visit_followup: Optional[str] = Field(None, alias="visit_followup")
    fulfilled_previous_recommendations: Optional[bool] = Field(
        None, alias="fulfilled_previous_recommendations"
    )
    new_recommendations: Optional[str] = Field(None, alias="new_recommendations")
    observations_seg: Optional[str] = Field(None, alias="observations_seg")
    register_coinnovation: Optional[str] = Field(None, alias="register_coinnovation")
    local_practice_tool_technology_coinnovation_identified: Optional[bool] = Field(
        None, alias="local_practice_tool_technology_coinnovation_identified"
    )
    local_coinovation_or_technology_record: Optional[bool] = Field(
        None, alias="local_coinovation_or_technology_record"
    )
    name_innovation: Optional[str] = Field(None, alias="name_innovation")
    description_innovation: Optional[str] = Field(None, alias="description_innovation")
    problem_solution_innovation: Optional[str] = Field(
        None, alias="problem_solution_innovation"
    )
    origin_and_developers: Optional[str] = Field(None, alias="origin_and_developers")
    materials_and_resources: Optional[str] = Field(
        None, alias="materials_and_resources"
    )
    process_functioning: Optional[str] = Field(None, alias="process_functioning")
    potential_replication: Optional[str] = Field(None, alias="potential_replication")
    observations_extensionist: Optional[str] = Field(
        None, alias="observations_extensionist"
    )
    date_hour_end: Optional[datetime] = Field(None, alias="date_hour_end")
    socilization_next_event: Optional[str] = Field(
        None, alias="socilization_next_event"
    )
    copy_documentation_delivered: Optional[bool] = Field(
        None, alias="copy_documentation_delivered"
    )

    class Config:
        from_attributes = True
        populate_by_name = True  # Allow population by field name or alias
