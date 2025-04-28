from repositories.audit_log_repository import AuditLogRepository
from src.audit_log import AuditLog

class InMemoryAuditLogRepository(AuditLogRepository):
    def __init__(self):
        self._storage = {}

    def save(self, audit_log: AuditLog) -> None:
        self._storage[audit_log._log_id] = audit_log

    def find_by_id(self, log_id: str) -> AuditLog:
        return self._storage.get(log_id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, log_id: str) -> None:
        if log_id in self._storage:
            del self._storage[log_id]
