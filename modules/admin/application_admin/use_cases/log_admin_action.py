from datetime import datetime
from sqlalchemy.orm import Session
from modules.admin.domain_admin.entities.admin_log_entity import AdminLog
from modules.admin.infrastructure_admin.repositories.admin_log_repository import (
    AdminLogRepository,
)


class LogAdminAction:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.admin_log_repository = AdminLogRepository(db_session)

    def execute(self, admin_user_id: int, action_id: int, description: str) -> AdminLog:
        log_entry = AdminLog(
            admin_user_id=admin_user_id,
            action_id=action_id,
            description=description,
            timestamp=datetime.now(),
        )
        return self.admin_log_repository.log_action(log_entry)
