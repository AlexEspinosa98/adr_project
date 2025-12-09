from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from common.domain.enums.survey_status import SurveyStatus
from modules.surveys.domain_surveys.entities.user_producter_entity import UserProducter
from modules.surveys.domain_surveys.entities.product_property_entity import (
    ProductProperty,
)


class Survey2(BaseModel):
    id: Optional[int] = Field(
        None, gt=0, description="Unique identifier for the entity"
    )
    extensionist_id: Optional[int]
    producter_id: Optional[int]
    producter: Optional[UserProducter]
    property_id: Optional[int]
    property: Optional[ProductProperty]
    objective_accompaniment: Optional[str]
    visit_development_follow_up_activities: Optional[str]
    previous_visit_recommendations_fulfilled: Optional[bool]
    recommendations_commitments: Optional[str]
    observations_visited: Optional[str]
    objective: Optional[str]
    visit_followup: Optional[str]
    fulfilled_previous_recommendations: Optional[bool]
    new_recommendations: Optional[str]
    observations_seg: Optional[str]
    register_coinnovation: Optional[str]
    local_practice_tool_technology_coinnovation_identified: Optional[bool]
    local_coinovation_or_technology_record: Optional[bool]
    name_innovation: Optional[str]
    description_innovation: Optional[str]
    problem_solution_innovation: Optional[str]
    origin_and_developers: Optional[str]
    materials_and_resources: Optional[str]
    process_functioning: Optional[str]
    potential_replication: Optional[str]
    observations_extensionist: Optional[str]
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
    phono_extra_1: Optional[str]
    file_pdf: Optional[str] = None
    date_hour_end: Optional[datetime]
    socilization_next_event: Optional[str]
    visit_date: Optional[datetime]
    attended_by: Optional[str]
    state: SurveyStatus

    # Data companionship
    date_acompanamiento: Optional[str] = None
    hour_acompanamiento: Optional[str] = None
    origen_register: Optional[str] = None
    name_acompanamiento: Optional[str] = None

    class Config:
        from_attributes = True
