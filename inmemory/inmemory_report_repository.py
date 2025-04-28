from repositories.report_repository import ReportRepository
from src.report import Report

class InMemoryReportRepository(ReportRepository):
    def __init__(self):
        self._storage = {}

    def save(self, report: Report) -> None:
        self._storage[report._report_id] = report

    def find_by_id(self, report_id: str) -> Report:
        return self._storage.get(report_id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, report_id: str) -> None:
        if report_id in self._storage:
            del self._storage[report_id]
