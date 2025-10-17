from sqlalchemy import String, Text, Integer, Date, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from common.infrastructure.database.models.base import BaseModel
from common.domain.enums.survey_status import SurveyStatus
from sqlalchemy.dialects.postgresql import JSONB


class UserProducter(BaseModel):

    __tablename__ = "user_producter"

    # metadata
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    type_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    identification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    # group focal
    is_woman_rural: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_young_rural: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    ethnic_belonging: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    is_victim_conflict: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_narp: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)


class ProductProperty(BaseModel):

    __tablename__ = "product_property"

    # Metadata
    # fk with user_producter
    user_producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    latitude: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    longitude: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    asnm: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    total_area: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    village: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    area_total_property: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    linea_productive_primary: Mapped[Optional[str]] = mapped_column(String(255))
    area_total_linea_productive_primary: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    linea_productive_secondary: Mapped[Optional[str]] = mapped_column(String(255))
    area_total_linea_productive_secondary: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    area_in_production: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


# ==============================
# Survey 1 - Diagnóstico Inicial
# ==============================
class Survey1(BaseModel):
    __tablename__ = "survey_1"

    extensionist_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_extensionist.id"))
    user_producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(ForeignKey("product_property.id"))

    classification_user: Mapped[Optional[dict]] = mapped_column(JSONB)
    medition_focalization: Mapped[Optional[dict]] = mapped_column(JSONB)

    #6.
    objetive_accompaniment: Mapped[Optional[str]] = mapped_column(String(500))
    initial_diagnosis: Mapped[Optional[str]] = mapped_column(String(500))
    recommendations_commitments: Mapped[Optional[str]] = mapped_column(String(500))
    observations: Mapped[Optional[str]] = mapped_column(String(500))

    # 7. data companionship
    visit_date: Mapped[Optional[datetime]] = mapped_column(Date)
    attended_by: Mapped[Optional[str]] = mapped_column(String(100))
    user: Mapped[Optional[str]] = mapped_column(String(100))
    worker_up: Mapped[Optional[str]] = mapped_column(String(50))
    Household_size: Mapped[Optional[str]] = mapped_column(String(10))
    other: Mapped[Optional[str]] = mapped_column(String(150))
    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    phono_extra_1: Mapped[Optional[str]] = mapped_column(String(255))
    state: Mapped[SurveyStatus] = mapped_column(Enum(SurveyStatus, name="survey_status"), default=SurveyStatus.PENDING)

# ==============================
# Survey 2 - Seguimiento y Co-Innovación
# ==============================
class Survey2(BaseModel):
    __tablename__ = "survey_2"

    extensionist_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_extensionist.id"))
    producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(ForeignKey("product_property.id"))

    objective_accompaniment: Mapped[Optional[str]] = mapped_column(String(500))
    visit_development_follow_up_activities: Mapped[Optional[str]] = mapped_column(String(500))
    previous_visit_recommendations_fulfilled: Mapped[Optional[bool]] = mapped_column(Boolean)
    recommendations_commitments: Mapped[Optional[str]] = mapped_column(String(500))
    observations: Mapped[Optional[str]] = mapped_column(String(700))

    # Seguimiento visita anterior
    objective: Mapped[Optional[str]] = mapped_column(String(500))
    visit_followup: Mapped[Optional[str]] = mapped_column(String(500))  # avances, dificultades, pendientes
    fulfilled_previous_recommendations: Mapped[Optional[bool]]
    new_recommendations: Mapped[Optional[str]] = mapped_column(String(500))
    observations_seg: Mapped[Optional[str]] = mapped_column(String(500))

    # 4. Co-innovación
    register_coinnovation: Mapped[Optional[str]] = mapped_column(String(500))
    local_practice_tool_technology_coinnovation_identified: Mapped[Optional[bool]] = mapped_column(Boolean)
    local_practice_tool_technology_coinnovation_identified: Mapped[Optional[bool]] = mapped_column(Boolean)
    local_coinovation_or_technology_record: Mapped[Optional[bool]] = mapped_column(Boolean)

    name_innovation: Mapped[Optional[str]] = mapped_column(String(150))
    description_innovation: Mapped[Optional[str]] = mapped_column(String(500))
    problem_solution_innovation: Mapped[Optional[str]] = mapped_column(String(500))
    origin_and_developers: Mapped[Optional[str]] = mapped_column(String(500))
    materials_and_resources: Mapped[Optional[str]] = mapped_column(String(500))
    process_functioning: Mapped[Optional[str]] = mapped_column(String(500))
    potential_replication: Mapped[Optional[str]] = mapped_column(String(500))
    observations_extensionist: Mapped[Optional[str]] = mapped_column(String(500))
    
    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    phono_extra_1: Mapped[Optional[str]] = mapped_column(String(255))

    # cierre
    date_hour_end: Mapped[Optional[datetime]] = mapped_column(Date)
    socilization_next_event: Mapped[Optional[str]] = mapped_column(String(500))
    copy_documentation_delivered: Mapped[Optional[bool]] = mapped_column(Boolean)

    # 7. data companionship
    visit_date: Mapped[Optional[datetime]] = mapped_column(Date)
    attended_by: Mapped[Optional[str]] = mapped_column(String(100))
    user: Mapped[Optional[str]] = mapped_column(String(100))
    worker_up: Mapped[Optional[str]] = mapped_column(String(50))
    Household_size: Mapped[Optional[str]] = mapped_column(String(10))
    other: Mapped[Optional[str]] = mapped_column(String(150))
    state: Mapped[SurveyStatus] = mapped_column(Enum(SurveyStatus, name="survey_status"), default=SurveyStatus.PENDING)


# ==============================
# Survey 3 - Diagnóstico Final
# ==============================
class Survey3(BaseModel):
    __tablename__ = "survey_3"

    extensionist_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_extensionist.id"))
    user_producter_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_producter.id"))
    property_id: Mapped[Optional[int]] = mapped_column(ForeignKey("product_property.id"))

    classification_user: Mapped[Optional[dict]] = mapped_column(JSONB)
    medition_focalization: Mapped[Optional[dict]] = mapped_column(JSONB)

    #6.
    objetive_accompaniment: Mapped[Optional[str]] = mapped_column(String(500))
    initial_diagnosis: Mapped[Optional[str]] = mapped_column(String(500))
    recommendations_commitments: Mapped[Optional[str]] = mapped_column(String(500))
    observations: Mapped[Optional[str]] = mapped_column(String(500))

    # 7. data companionship
    visit_date: Mapped[Optional[datetime]] = mapped_column(Date)
    attended_by: Mapped[Optional[str]] = mapped_column(String(100))
    user: Mapped[Optional[str]] = mapped_column(String(100))
    worker_up: Mapped[Optional[str]] = mapped_column(String(50))
    Household_size: Mapped[Optional[str]] = mapped_column(String(10))
    other: Mapped[Optional[str]] = mapped_column(String(150))
    # Fotos
    photo_user: Mapped[Optional[str]] = mapped_column(String(255))
    photo_interaction: Mapped[Optional[str]] = mapped_column(String(255))
    photo_panorama: Mapped[Optional[str]] = mapped_column(String(255))
    phono_extra_1: Mapped[Optional[str]] = mapped_column(String(255))
    state: Mapped[SurveyStatus] = mapped_column(Enum(SurveyStatus, name="survey_status"), default=SurveyStatus.PENDING)
