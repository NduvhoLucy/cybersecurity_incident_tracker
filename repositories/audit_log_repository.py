from repositories.repository import Repository
from src.audit_log import AuditLog

class AuditLogRepository(Repository[AuditLog, str]):
    pass
