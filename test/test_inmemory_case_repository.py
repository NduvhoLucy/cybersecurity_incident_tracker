from repositories.inmemory.inmemory_case_repository import InMemoryCaseRepository
from src.case import Case

def test_case_crud_operations():
    repo = InMemoryCaseRepository()
    case = Case("C001", "I001", "analyst123")

    repo.save(case)
    assert repo.find_by_id("C001")._incident_id == "I001"
    assert len(repo.find_all()) == 1

    repo.delete("C001")
    assert repo.find_by_id("C001") is None
