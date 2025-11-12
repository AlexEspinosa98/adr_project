from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CreateSurvey1OutputDTO(BaseModel):
    id: int
    extensionist_id: Optional[int]
    producter_id: Optional[int]
    property_id: Optional[int]
    visit_date: Optional[datetime]
    attended_by: Optional[str]
    attended_role: Optional[str]
    human_technical_capacities: Optional[str]
    social_associativity: Optional[str]
    technology_access: Optional[str]
    natural_resources_management: Optional[str]
    public_policy_participation: Optional[str]
    is_woman_rural: Optional[bool]
    is_young_rural: Optional[bool]
    ethnic_belonging: Optional[bool]
    is_narp: Optional[bool]
    is_victim_conflict: Optional[bool]
    control_resources: Optional[int]
    control_resources_obs: Optional[str]
    decision_voice: Optional[int]
    decision_voice_obs: Optional[str]
    innovation_leadership: Optional[int]
    innovation_leadership_obs: Optional[str]
    knowledge_dialogue: Optional[int]
    knowledge_dialogue_obs: Optional[str]
    objective: Optional[str]
    initial_diagnosis: Optional[str]
    recommendations: Optional[str]
    observations: Optional[str]
    photo_user: Optional[str]
    photo_interaction: Optional[str]
    photo_panorama: Optional[str]
