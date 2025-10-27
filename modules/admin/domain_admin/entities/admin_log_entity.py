from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .action_entity import Action
from modules.admin.domain_admin.entities.admin_user_entity import AdminUser

class AdminLog(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    admin_user_id: int
    admin_user: Optional[AdminUser]
    action_id: int
    action: Optional[Action]
    entity: str
    entity_id: int
    old_value: Optional[str]
    new_value: Optional[str]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
