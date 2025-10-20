from common.infrastructure.database.models.base import BaseModel
from typing import Optional

from sqlalchemy import String, Text, Integer,Date,Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class AdminUser(BaseModel):
    __tablename__ =  "user_admin"
    # metadata
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    rol: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    identification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    