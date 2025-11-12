"""
Database infrastructure module.

Import all models here to ensure they are registered with SQLAlchemy.
"""

# Import all models to register them with SQLAlchemy
from .base import Base, BaseModel
from .auth import UserExtensionist
from .survey import (
    UserProducter,
    ProductProperty,
    Survey1,
    Survey2,
    Survey3,
    ClassificationUser,
)
from .admin import AdminUser, ActionsLog, AdminLogger


__all__: list[str] = [
    "Base",
    "BaseModel",
    "UserExtensionist",
    "UserProducter",
    "ProductProperty",
    "Survey1",
    "Survey2",
    "Survey3",
    "ClassificationUser",
    "AdminUser",
    "ActionsLog",
    "AdminLogger",
]
