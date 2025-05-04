from repositories.inmemory.audit_log_inmemory_repository import InMemoryAuditLogRepository
from src.audit_log import AuditLog

class AuditLogService:
    def __init__(self, repository=None):
        self.repository = repository or InMemoryAuditLogRepository()

    def record_log(self, log: AuditLog):
        if not log.id or not log.action:
            raise ValueError("Audit log must have an ID and an action.")
        self.repository.save(log)

    def get_log(self, log_id: str):
        return self.repository.find_by_id(log_id)

    def list_all_logs(self):
        return self.repository.find_all()

    def delete_log(self, log_id: str):
        self.repository.delete(log_id)
