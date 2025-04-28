from repositories.inmemory.inmemory_audit_log_repository import InMemoryAuditLogRepository
from src.audit_log import AuditLog

def test_audit_log_crud_operations():
    repo = InMemoryAuditLogRepository()
    audit_log = AuditLog("L001", "2024-04-26T12:00:00Z", "Login", "user123")

    repo.save(audit_log)
    assert repo.find_by_id("L001")._action == "Login"
    assert len(repo.find_all()) == 1

    repo.delete("L001")
    assert repo.find_by_id("L001") is None
