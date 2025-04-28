from repositories.inmemory.inmemory_report_repository import InMemoryReportRepository
from src.report import Report

def test_report_crud_operations():
    repo = InMemoryReportRepository()
    report = Report("R001", "Incident Summary", "manager1", "2024-04-26", "Incident details here")

    repo.save(report)
    assert repo.find_by_id("R001")._type == "Incident Summary"
    assert len(repo.find_all()) == 1

    repo.delete("R001")
    assert repo.find_by_id("R001") is None
