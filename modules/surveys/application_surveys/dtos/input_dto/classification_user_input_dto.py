from pydantic import BaseModel
from typing import Optional


class ClassificationUserInputDTO(BaseModel):
    main_productive_activity: Optional[int] = None
    secondary_productive_activities: Optional[int] = None
    tools_and_equipment: Optional[int] = None
    good_agricultural_practices: Optional[int] = None
    commercialization_structure: Optional[int] = None
    markets: Optional[int] = None
    added_value: Optional[int] = None
    records: Optional[int] = None
    labor_type: Optional[int] = None
    credit_and_banking: Optional[int] = None
    organization_membership: Optional[int] = None
    collective_activities: Optional[int] = None
    entrepreneurship_associativity: Optional[int] = None
    commercial_alliances: Optional[int] = None
    technical_support: Optional[int] = None
    quality_certifications: Optional[int] = None
    intellectual_property: Optional[int] = None
    access_information_sources: Optional[int] = None
    access_to_ict: Optional[int] = None
    use_of_ict_decision: Optional[int] = None
    ict_skills: Optional[int] = None
    knowledge_appropriation: Optional[int] = None
    environmental_practices: Optional[int] = None
    sustainable_practices: Optional[int] = None
    climate_change_adaptation: Optional[int] = None
    environmental_regulations: Optional[int] = None
    participation_mechanisms: Optional[int] = None
    participation_tools: Optional[int] = None
    political_social_control: Optional[int] = None
    community_self_management: Optional[int] = None
