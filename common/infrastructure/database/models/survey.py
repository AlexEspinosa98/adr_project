from sqlalchemy import String, Text, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from common.infrastructure.database.models.base import BaseModel


# ==============================
# Survey 1 - Diagnóstico Inicial
# ==============================
class Survey1(BaseModel):
    __tablename__ = "survey_1"

    extensionist_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_extensionist.id"))
    producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(ForeignKey("product_property.id"))

    visit_date: Mapped[Optional[datetime]] = mapped_column(Date)
    attended_by: Mapped[Optional[str]] = mapped_column(String(255))
    attended_role: Mapped[Optional[str]] = mapped_column(String(100))

    # Clasificación usuario
    human_technical_capacities: Mapped[Optional[Text]]
    social_associativity: Mapped[Optional[Text]]
    technology_access: Mapped[Optional[Text]]
    natural_resources_management: Mapped[Optional[Text]]
    public_policy_participation: Mapped[Optional[Text]]

    # Grupo focal
    is_woman_rural: Mapped[Optional[bool]]
    is_young_rural: Mapped[Optional[bool]]
    ethnic_belonging: Mapped[Optional[bool]]
    is_narp: Mapped[Optional[bool]]
    is_victim_conflict: Mapped[Optional[bool]]

    # Matriz focalización
    control_resources: Mapped[Optional[int]]
    control_resources_obs: Mapped[Optional[Text]]
    decision_voice: Mapped[Optional[int]]
    decision_voice_obs: Mapped[Optional[Text]]
    innovation_leadership: Mapped[Optional[int]]
    innovation_leadership_obs: Mapped[Optional[Text]]
    knowledge_dialogue: Mapped[Optional[int]]
    knowledge_dialogue_obs: Mapped[Optional[Text]]

    # Técnico productivo
    objective: Mapped[Optional[Text]]
    initial_diagnosis: Mapped[Optional[Text]]
    recommendations: Mapped[Optional[Text]]
    observations: Mapped[Optional[Text]]

    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))


# ==============================
# Survey 2 - Seguimiento y Co-Innovación
# ==============================
class Survey2(BaseModel):
    __tablename__ = "survey_2"

    extensionist_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_extensionist.id"))
    producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(ForeignKey("product_property.id"))

    visit_date: Mapped[Optional[datetime]] = mapped_column(Date)
    attended_by: Mapped[Optional[str]] = mapped_column(String(255))
    attended_role: Mapped[Optional[str]] = mapped_column(String(100))

    # Seguimiento visita anterior
    objective: Mapped[Optional[Text]]
    visit_followup: Mapped[Optional[Text]]  # avances, dificultades, pendientes
    fulfilled_previous_recommendations: Mapped[Optional[bool]]
    new_recommendations: Mapped[Optional[Text]]
    observations: Mapped[Optional[Text]]

    # Co-innovación
    co_innovation_identified: Mapped[Optional[bool]]
    co_innovation_consent: Mapped[Optional[bool]]
    innovation_name: Mapped[Optional[str]] = mapped_column(String(255))
    innovation_description: Mapped[Optional[Text]]
    innovation_problem_solved: Mapped[Optional[Text]]
    innovation_origin: Mapped[Optional[str]]
    innovation_materials: Mapped[Optional[Text]]
    innovation_process: Mapped[Optional[Text]]
    innovation_scalability: Mapped[Optional[Text]]
    innovation_observations: Mapped[Optional[Text]]

    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    photo_innovation_1: Mapped[Optional[str]] = mapped_column(String(255))
    photo_innovation_2: Mapped[Optional[str]] = mapped_column(String(255))
    photo_innovation_3: Mapped[Optional[str]] = mapped_column(String(255))
    photo_innovation_4: M-apped[Optional[str]] = mapped_column(String(255))


# ==============================
# Survey 3 - Diagnóstico Final
# ==============================
class Survey3(BaseModel):
    __tablename__ = "survey_3"

    extensionist_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_extensionist.id"))
    producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(ForeignKey("product_property.id"))

    visit_date: Mapped[Optional[datetime]] = mapped_column(Date)
    attended_by: Mapped[Optional[str]] = mapped_column(String(255))
    attended_role: Mapped[Optional[str]] = mapped_column(String(100))

    # Clasificación del usuario (misma lógica que V1, pero ahora con resultados finales)
    human_technical_capacities: Mapped[Optional[Text]]
    social_associativity: Mapped[Optional[Text]]
    technology_access: Mapped[Optional[Text]]
    natural_resources_management: Mapped[Optional[Text]]
    public_policy_participation: Mapped[Optional[Text]]

    # Grupo focal con evidencia de cambio
    is_woman_rural: Mapped[Optional[bool]]
    is_young_rural: Mapped[Optional[bool]]
    ethnic_belonging: Mapped[Optional[bool]]
    is_narp: Mapped[Optional[bool]]
    is_victim_conflict: Mapped[Optional[bool]]

    control_resources: Mapped[Optional[int]]
    control_resources_evidence: Mapped[Optional[Text]]
    decision_voice: Mapped[Optional[int]]
    decision_voice_evidence: Mapped[Optional[Text]]
    innovation_leadership: Mapped[Optional[int]]
    innovation_leadership_evidence: Mapped[Optional[Text]]
    knowledge_dialogue: Mapped[Optional[int]]
    knowledge_dialogue_evidence: Mapped[Optional[Text]]

    # Técnico productivo
    objective: Mapped[Optional[Text]]
    development: Mapped[Optional[Text]]  # descripción del acompañamiento
    final_diagnosis: Mapped[Optional[Text]]
    fulfilled_previous_recommendations: Mapped[Optional[bool]]
    observations: Mapped[Optional[Text]]

    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_development: Mapped[Optional[str]] = mapped_column(String(255))