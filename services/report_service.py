from repositories.inmemory.report_inmemory_repository import InMemoryReportRepository
from src.report import Report

class ReportService:
    def __init__(self, repository=None):
        self.repository = repository or InMemoryReportRepository()

    def generate_report(self, report: Report):
        if not report.id or not report.summary:
            raise ValueError("Report must have an ID and summary.")
        self.repository.save(report)

    def get_report(self, report_id: str):
        return self.repository.find_by_id(report_id)

    def list_all_reports(self):
        return self.repository.find_all()

    def delete_report(self, report_id: str):
        self.repository.delete(report_id)
