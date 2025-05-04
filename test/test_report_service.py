import unittest
from services.report_service import ReportService
from repositories.inmemory.inmemory_report_repository import InMemoryReportRepository
from entities.report import Report


class TestReportService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryReportRepository()
        self.service = ReportService(self.repo)

    def test_create_and_get_report(self):
        report = Report(id="R001", incident_id="INC123", content="Detailed analysis", created_by="analyst1")
        self.service.create_report(report)
        retrieved = self.service.get_report_by_id("R001")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.id, "R001")
        self.assertEqual(retrieved.content, "Detailed analysis")

    def test_update_report(self):
        report = Report(id="R002", incident_id="INC456", content="Initial report", created_by="analyst2")
        self.service.create_report(report)

        report.content = "Updated content"
        self.service.update_report(report)

        updated = self.service.get_report_by_id("R002")
        self.assertEqual(updated.content, "Updated content")

    def test_delete_report(self):
        report = Report(id="R003", incident_id="INC789", content="To be deleted", created_by="analyst3")
        self.service.create_report(report)
        self.service.delete_report("R003")
        deleted = self.service.get_report_by_id("R003")
        self.assertIsNone(deleted)

    def test_get_all_reports(self):
        self.service.create_report(Report(id="R004", incident_id="INC111", content="R1", created_by="user1"))
        self.service.create_report(Report(id="R005", incident_id="INC112", content="R2", created_by="user2"))

        all_reports = self.service.get_all_reports()
        self.assertEqual(len(all_reports), 2)


if __name__ == '__main__':
    unittest.main()
