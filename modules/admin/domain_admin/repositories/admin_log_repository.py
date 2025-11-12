from abc import ABC, abstractmethod
from modules.admin.domain_admin.entities.admin_log_entity import AdminLog


class AdminLogRepository(ABC):
    @abstractmethod
    def log_action(self, log: AdminLog) -> AdminLog:
        pass
