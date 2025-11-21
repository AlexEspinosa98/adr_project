from pydantic import BaseModel, Field, validator
from typing import Optional, Union, Dict
import json
from datetime import datetime
from modules.surveys.application_surveys.dtos.output_dto.user_producter_output_dto import (
    UserProducterOutputDTO,
)
from modules.surveys.application_surveys.dtos.output_dto.product_property_output_dto import (
    ProductPropertyOutputDTO,
)


class Survey2DetailOutputDTO(BaseModel):
    id: int
    producter: Optional[UserProducterOutputDTO]
    property: Optional[ProductPropertyOutputDTO]
    objective_accompaniment: Optional[Union[Dict, str]] = Field(
        None, alias="objective_accompaniment"
    )
    visit_development_follow_up_activities: Optional[str] = Field(
        None, alias="visit_development_follow_up_activities"
    )
    previous_visit_recommendations_fulfilled: Optional[bool] = Field(
        None, alias="previous_visit_recommendations_fulfilled"
    )
    recommendations_commitments: Optional[str] = Field(
        None, alias="recommendations_commitments"
    )
    observations_visited: Optional[str] = Field(None, alias="observations_visited")
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
    photo_user: Optional[str] = Field(None, alias="photo_user")
    photo_interaction: Optional[str] = Field(None, alias="photo_interaction")
    photo_panorama: Optional[str] = Field(None, alias="photo_panorama")
    phono_extra_1: Optional[str] = Field(None, alias="phono_extra_1")
    date_hour_end: Optional[datetime] = Field(None, alias="date_hour_end")
    socilization_next_event: Optional[str] = Field(
        None, alias="socilization_next_event"
    )
    copy_documentation_delivered: Optional[bool] = Field(
        None, alias="copy_documentation_delivered"
    )
    visit_date: Optional[datetime] = Field(None, alias="visit_date")
    attended_by: Optional[str] = Field(None, alias="attended_by")
    state: Optional[str]

    # Data companionship
    date_acompanamiento: Optional[str] = None
    hour_acompanamiento: Optional[str] = None
    origen_register: Optional[str] = None
    name_acompanamiento: Optional[str] = None
    type_acompanamiento: Optional[str] = None
    other_acompanamiento: Optional[str] = None
    rejection_reason: Optional[str] = None

    @validator("objective_accompaniment", pre=True)
    def parse_json_fields(cls, value):
        if isinstance(value, str):
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError):
                return value
        return value

    class Config:
        from_attributes = True
        populate_by_name = True
