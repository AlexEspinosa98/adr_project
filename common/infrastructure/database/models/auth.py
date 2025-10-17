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
    signing_image_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    api_token: Mapped[Optional[str]] = mapped_column(String(255), unique=True, index=True, nullable=True)
