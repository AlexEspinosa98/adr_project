from typing import Optional
from datetime import datetime

from common.domain import entities as common_entities


class AdminLog(common_entities.BaseEntity):
    admin_user_id: int
    action_id: int
    description: str
    timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True