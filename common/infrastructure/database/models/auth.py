from common.infrastructure.database.models.base import BaseModel
from typing import Optional

from sqlalchemy import String, Text, Integer,Date,Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class UserExtensionist(BaseModel):
    __tablename__ =  "user_extensionist"

    # metadata
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    type_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    identification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    zone: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)


class UserProducter(BaseModel):

    __tablename__ = "user_producter"

    # metadata
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    type_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    identification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    is_woman_rural: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_young_rural: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    ethnic_belonging: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    is_victim_conflict: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_narp: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)


class ProductProperty(BaseModel):

    __tablename__ = "product_property"

    # Metadata
    # fk with user_producter
    user_producter_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    latitude: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    longitude: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    asnm: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    total_area: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    village: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)