import unittest
from services.audit_log_service import AuditLogService
from repositories.inmemory.audit_log_repository import InMemoryAuditLogRepository
from models.audit_log import AuditLog

class TestAuditLogService(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryAuditLogRepository()
        self.service = AuditLogService(self.repository)

    def test_log_and_retrieve_entry(self):
        log = AuditLog(log_id="L001", action="Login", user_id="U001")
        self.service.log_action(log)
        retrieved = self.service.get_log("L001")
        self.assertEqual(retrieved.action, "Login")

if __name__ == "__main__":
    unittest.main()
