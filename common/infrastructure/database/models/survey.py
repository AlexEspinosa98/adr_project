from sqlalchemy import String, Integer, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import Optional
from common.infrastructure.database.models.base import BaseModel
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.dialects.postgresql import JSONB
import json


class UserProducter(BaseModel):
    __tablename__ = "user_producter"

    # metadata
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    type_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    identification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    number_phone: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    # group focal
    is_woman_rural: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_young_rural: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    ethnic_belonging: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    is_victim_conflict: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_narp: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)

    # organization
    is_producer_organization_member: Mapped[Optional[bool]] = mapped_column(
        Boolean, nullable=True
    )
    organization_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    representantive1_name: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True
    )


class ProductProperty(BaseModel):
    __tablename__ = "product_property"

    # Metadata
    # fk with user_producter
    user_producter_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_producter.id"), nullable=True
    )
    # identify property
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    latitude: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    longitude: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    asnm: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    village: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # productive information
    linea_productive_primary: Mapped[Optional[str]] = mapped_column(String(255))
    linea_productive_secondary: Mapped[Optional[str]] = mapped_column(String(255))
    area_in_production: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


class ObjetcEvaluation(PydanticBaseModel):
    observation: Optional[str]
    score: Optional[int]

    class Config:
        extra = "allow"


class ClassificationUser(PydanticBaseModel):
    development_human_capacity: Optional[ObjetcEvaluation]
    development_social_capacity: Optional[ObjetcEvaluation]
    access_adaptative_adoption_information: Optional[ObjetcEvaluation]
    sustainable_management_natural_resources: Optional[ObjetcEvaluation]
    participation_public_political: Optional[ObjetcEvaluation]

    class config:
        extra = "allow"


class ResultFocalization(PydanticBaseModel):
    control_resources: Optional[ObjetcEvaluation]
    voice_influence_decision: Optional[ObjetcEvaluation]
    leadership_innovation: Optional[ObjetcEvaluation]
    dialogue_knowledge: Optional[ObjetcEvaluation]

    class Config:
        extra = "allow"


# ==============================
# Survey 1 - Diagnóstico Inicial
# ==============================
class Survey1(BaseModel):
    __tablename__ = "survey_1"

    extensionist_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_extensionist.id")
    )
    user_producter_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_producter.id")
    )
    property_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("product_property.id")
    )

    property: Mapped["ProductProperty"] = relationship(lazy="joined")
    user_producter: Mapped["UserProducter"] = relationship(
        foreign_keys=[user_producter_id],
        primaryjoin="Survey1.user_producter_id == UserProducter.id",
        lazy="joined",
    )

    classification_user: Mapped[Optional[dict]] = mapped_column(JSONB)
    medition_focalization: Mapped[Optional[dict]] = mapped_column(JSONB)

    # 6.
    objetive_accompaniment: Mapped[Optional[dict]] = mapped_column(JSONB)
    initial_diagnosis: Mapped[Optional[str]] = mapped_column(String(500))
    recommendations_commitments: Mapped[Optional[str]] = mapped_column(String(500))
    observations_visited: Mapped[Optional[str]] = mapped_column(String(500))

    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    phono_extra_1: Mapped[Optional[str]] = mapped_column(String(255))
    state: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=False, default="PENDING"
    )

    # closed and despedida
    date_hour_end: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    copy_documentation_delivered: Mapped[Optional[str]] = mapped_column(String(50))

    # Date acompañamiento
    date_acompanamiento: Mapped[Optional[str]] = mapped_column(String(50))
    hour_acompanamiento: Mapped[Optional[str]] = mapped_column(String(50))
    origen_register: Mapped[Optional[str]] = mapped_column(String(100))
    name_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))
    type_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))
    other_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))

    # Otros campos
    visit_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    attended_by: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    def set_classification_user(self, data: dict):
        validated = ClassificationUser(**data)
        self.classification_user = validated.model_dump()

    def get_classification_user(self) -> ClassificationUser:
        if self.classification_user:
            if isinstance(self.classification_user, str):
                return ClassificationUser(**json.loads(self.classification_user))
            return ClassificationUser(**self.classification_user)
        return None

    def set_medition_focalization(self, data: dict):
        validated = ResultFocalization(**data)
        self.medition_focalization = validated.model_dump()

    def get_medition_focalization(self) -> ResultFocalization:
        if self.medition_focalization:
            if isinstance(self.medition_focalization, str):
                return ResultFocalization(**json.loads(self.medition_focalization))
            return ResultFocalization(**self.medition_focalization)
        return None


# ==============================
# Survey 2 - Seguimiento y Co-Innovación
# ==============================
class Survey2(BaseModel):
    __tablename__ = "survey_2"

    extensionist_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_extensionist.id")
    )
    producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("product_property.id")
    )

    producter: Mapped["UserProducter"] = relationship(
        foreign_keys=[producter_id],
        primaryjoin="Survey2.producter_id == UserProducter.id",
        lazy="joined",
    )
    property: Mapped["ProductProperty"] = relationship(lazy="joined")

    objective_accompaniment: Mapped[Optional[dict]] = mapped_column(JSONB)
    visit_development_follow_up_activities: Mapped[Optional[str]] = mapped_column(
        String(500)
    )
    previous_visit_recommendations_fulfilled: Mapped[Optional[bool]] = mapped_column(
        Boolean
    )
    recommendations_commitments: Mapped[Optional[str]] = mapped_column(String(500))
    observations_visited: Mapped[Optional[str]] = mapped_column(String(700))

    # Seguimiento visita anterior
    objective: Mapped[Optional[str]] = mapped_column(String(500))
    visit_followup: Mapped[Optional[str]] = mapped_column(
        String(500)
    )  # avances, dificultades, pendientes
    fulfilled_previous_recommendations: Mapped[Optional[bool]] = mapped_column(
        Boolean, nullable=True
    )
    new_recommendations: Mapped[Optional[str]] = mapped_column(String(500))
    observations_seg: Mapped[Optional[str]] = mapped_column(String(500))

    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    phono_extra_1: Mapped[Optional[str]] = mapped_column(String(255))

    # 4. Co-innovación
    register_coinnovation: Mapped[Optional[str]] = mapped_column(String(500))
    local_practice_tool_technology_coinnovation_identified: Mapped[Optional[bool]] = (
        mapped_column(Boolean)
    )
    local_coinovation_or_technology_record: Mapped[Optional[bool]] = mapped_column(
        Boolean
    )

    name_innovation: Mapped[Optional[str]] = mapped_column(String(150))
    description_innovation: Mapped[Optional[str]] = mapped_column(String(500))
    problem_solution_innovation: Mapped[Optional[str]] = mapped_column(String(500))
    origin_and_developers: Mapped[Optional[str]] = mapped_column(String(500))
    materials_and_resources: Mapped[Optional[str]] = mapped_column(String(500))
    process_functioning: Mapped[Optional[str]] = mapped_column(String(500))
    potential_replication: Mapped[Optional[str]] = mapped_column(String(500))
    observations_extensionist: Mapped[Optional[str]] = mapped_column(String(500))

    # cierre
    date_hour_end: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    socilization_next_event: Mapped[Optional[str]] = mapped_column(String(500))
    copy_documentation_delivered: Mapped[Optional[bool]] = mapped_column(Boolean)

    # 7. data companionship
    date_acompanamiento: Mapped[Optional[str]] = mapped_column(String(50))
    hour_acompanamiento: Mapped[Optional[str]] = mapped_column(String(50))
    origen_register: Mapped[Optional[str]] = mapped_column(String(100))
    name_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))
    type_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))
    other_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))

    state: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=False, default="PENDING"
    )

    # Otros campos
    visit_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    attended_by: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)


# ==============================
# Survey 3 - Diagnóstico Final
# ==============================
class Survey3(BaseModel):
    __tablename__ = "survey_3"

    extensionist_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_extensionist.id")
    )
    user_producter_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_producter.id")
    )
    property_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("product_property.id")
    )

    property: Mapped["ProductProperty"] = relationship(lazy="joined")
    user_producter: Mapped["UserProducter"] = relationship(
        foreign_keys=[user_producter_id],
        primaryjoin="Survey3.user_producter_id == UserProducter.id",
        lazy="joined",
    )

    classification_user: Mapped[Optional[dict]] = mapped_column(JSONB)
    medition_focalization: Mapped[Optional[dict]] = mapped_column(JSONB)

    # 6.
    objetive_accompaniment: Mapped[Optional[dict]] = mapped_column(JSONB)
    development_accompaniment: Mapped[Optional[str]] = mapped_column(String(500))
    final_diagnosis: Mapped[Optional[str]] = mapped_column(String(500))
    recommendations_commitments: Mapped[Optional[str]] = mapped_column(String(500))
    observations_visited: Mapped[Optional[str]] = mapped_column(String(500))

    # 7. data companionship
    date_acompanamiento: Mapped[Optional[str]] = mapped_column(String(50))
    hour_acompanamiento: Mapped[Optional[str]] = mapped_column(String(50))
    origen_register: Mapped[Optional[str]] = mapped_column(String(100))
    name_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))
    type_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))
    other_acompanamiento: Mapped[Optional[str]] = mapped_column(String(100))

    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    phono_extra_1: Mapped[Optional[str]] = mapped_column(String(255))
    state: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=False, default="PENDING"
    )

    # closed and despedida
    date_hour_end: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    copy_documentation_delivered: Mapped[Optional[str]] = mapped_column(String(50))
    socialization_events_group: Mapped[Optional[str]] = mapped_column(String(500))
    not_agend_new_visit: Mapped[Optional[str]] = mapped_column(String(500))

    # Otros campos
    visit_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    attended_by: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    def set_classification_user(self, data: dict):
        validated = ClassificationUser(**data)
        self.classification_user = validated.model_dump()

    def get_classification_user(self) -> ClassificationUser:
        if self.classification_user:
            if isinstance(self.classification_user, str):
                return ClassificationUser(**json.loads(self.classification_user))
            return ClassificationUser(**self.classification_user)
        return None

    def set_medition_focalization(self, data: dict):
        validated = ResultFocalization(**data)
        self.medition_focalization = validated.model_dump()

    def get_medition_focalization(self) -> ResultFocalization:
        if self.medition_focalization:
            if isinstance(self.medition_focalization, str):
                return ResultFocalization(**json.loads(self.medition_focalization))
            return ResultFocalization(**self.medition_focalization)
        return None


class ClassificationUser(BaseModel):
    __tablename__ = "classification_user"

    survey_idd1: Mapped[Optional[int]] = mapped_column(
        ForeignKey("survey_1.id")
    )  # cambiar esta relacion en el futuro
    survey_idd3: Mapped[Optional[int]] = mapped_column(ForeignKey("survey_3.id"))
    # Aspect 1 - Human and Technical Capacities
    main_productive_activity: Mapped[Optional[int]] = mapped_column(Integer)  # Q1
    secondary_productive_activities: Mapped[Optional[int]] = mapped_column(
        Integer
    )  # Q2
    tools_and_equipment: Mapped[Optional[int]] = mapped_column(Integer)  # Q3
    good_agricultural_practices: Mapped[Optional[int]] = mapped_column(Integer)  # Q4
    commercialization_structure: Mapped[Optional[int]] = mapped_column(Integer)  # Q5
    markets: Mapped[Optional[int]] = mapped_column(Integer)  # Q6
    added_value: Mapped[Optional[int]] = mapped_column(Integer)  # Q7
    records: Mapped[Optional[int]] = mapped_column(Integer)  # Q8
    labor_type: Mapped[Optional[int]] = mapped_column(Integer)  # Q9
    credit_and_banking: Mapped[Optional[int]] = mapped_column(Integer)  # Q10

    # Aspect 2 - Social Capacities & Associativity
    organization_membership: Mapped[Optional[int]] = mapped_column(Integer)  # Q11
    collective_activities: Mapped[Optional[int]] = mapped_column(Integer)  # Q12
    entrepreneurship_associativity: Mapped[Optional[int]] = mapped_column(
        Integer
    )  # Q13
    commercial_alliances: Mapped[Optional[int]] = mapped_column(Integer)  # Q14
    technical_support: Mapped[Optional[int]] = mapped_column(Integer)  # Q15
    quality_certifications: Mapped[Optional[int]] = mapped_column(Integer)  # Q16
    intellectual_property: Mapped[Optional[int]] = mapped_column(Integer)  # Q17

    # Aspect 3 - Information & ICT
    access_information_sources: Mapped[Optional[int]] = mapped_column(Integer)  # Q18
    access_to_ict: Mapped[Optional[int]] = mapped_column(Integer)  # Q19
    use_of_ict_decision: Mapped[Optional[int]] = mapped_column(Integer)  # Q20
    ict_skills: Mapped[Optional[int]] = mapped_column(Integer)  # Q21
    knowledge_appropriation: Mapped[Optional[int]] = mapped_column(Integer)  # Q22

    # Aspect 4 - Sustainable Resource Management
    environmental_practices: Mapped[Optional[int]] = mapped_column(Integer)  # Q23
    sustainable_practices: Mapped[Optional[int]] = mapped_column(Integer)  # Q24
    climate_change_adaptation: Mapped[Optional[int]] = mapped_column(Integer)  # Q25
    environmental_regulations: Mapped[Optional[int]] = mapped_column(Integer)  # Q26

    # Aspect 5 - Participation & Empowerment
    participation_mechanisms: Mapped[Optional[int]] = mapped_column(Integer)  # Q27
    participation_tools: Mapped[Optional[int]] = mapped_column(Integer)  # Q28
    political_social_control: Mapped[Optional[int]] = mapped_column(Integer)  # Q29
    community_self_management: Mapped[Optional[int]] = mapped_column(Integer)  # Q30


class SurveyRejection(BaseModel):
    __tablename__ = "survey_rejection"

    survey_id: Mapped[int] = mapped_column(Integer, nullable=False)
    survey_type: Mapped[int] = mapped_column(Integer, nullable=False)
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    admin_user_id: Mapped[int] = mapped_column(ForeignKey("user_admin.id"), nullable=False)
