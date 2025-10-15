from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .survey_user_extensionist import SurveyUserExtensionistInputDTO
from .survey_user_producter import SurveyUserProducterInputDTO

class CreateSurvey1InputDTO(BaseModel):
    extensionist: SurveyUserExtensionistInputDTO
    producter: SurveyUserProducterInputDTO
    property_id: int
    visit_date: Optional[datetime] = None
    attended_by: Optional[str] = None
    attended_role: Optional[str] = None
    human_technical_capacities: Optional[str] = None
    social_associativity: Optional[str] = None
    technology_access: Optional[str] = None
    natural_resources_management: Optional[str] = None
    public_policy_participation: Optional[str] = None
    is_woman_rural: Optional[bool] = None
    is_young_rural: Optional[bool] = None
    ethnic_belonging: Optional[bool] = None
    is_narp: Optional[bool] = None
    is_victim_conflict: Optional[bool] = None
    control_resources: Optional[int] = None
    control_resources_obs: Optional[str] = None
    decision_voice: Optional[int] = None
    decision_voice_obs: Optional[str] = None
    innovation_leadership: Optional[int] = None
    innovation_leadership_obs: Optional[str] = None
    knowledge_dialogue: Optional[int] = None
    knowledge_dialogue_obs: Optional[str] = None
    objective: Optional[str] = None
    initial_diagnosis: Optional[str] = None
    recommendations: Optional[str] = None
    observations: Optional[str] = None
    photo_user: Optional[str] = None
    photo_interaction: Optional[str] = None
    photo_panorama: Optional[str] = None
