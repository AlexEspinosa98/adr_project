from common.infrastructure.database.models.base import BaseModel
from typing import Optional

from sqlalchemy import String, Integer, Date, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AdminUser(BaseModel):
    __tablename__ = "user_admin"
    # metadata
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(
        String(255), unique=True, index=True, nullable=True
    )
    password: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    rol: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    identification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    token_register: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)


class ActionsLog(BaseModel):
    __tablename__ = "actions_log"
    # metadata
    action: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    timestamp: Mapped[Optional[Date]] = mapped_column(Date, nullable=True)


class AdminLogger(BaseModel):
    __tablename__ = "admin_logger"
    # metadata
    # fk with admin_user
    admin_user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("user_admin.id"), nullable=True
    )

    admin_user: Mapped[Optional[AdminUser]] = relationship("AdminUser")
    action: Mapped[Optional[int]] = mapped_column(
        ForeignKey("actions_log.id"), nullable=True
    )
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    timestamp: Mapped[Optional[Date]] = mapped_column(Date, nullable=True)
