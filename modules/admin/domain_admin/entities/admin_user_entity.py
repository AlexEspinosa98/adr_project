from typing import Optional
from common.domain import entities as common_entities
from pydantic import Field

class AdminUser(common_entities.BaseEntity):
    name: Optional[str] = Field(None, description="Admin user name")
    last_name: Optional[str] = Field(None, description="Admin user last name")
    email: Optional[str] = Field(None, description="Admin user email")
    password: Optional[str] = Field(None, description="Admin user password (hashed)")
    phone: Optional[str] = Field(None, description="Admin user phone")
    rol: Optional[str] = Field(None, description="Admin user role")
    identification: Optional[str] = Field(None, description="Admin user identification")
    token_register: Optional[str] = Field(None, description="Admin user registration token")
