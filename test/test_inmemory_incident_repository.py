from repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from src.incident import Incident

def test_incident_crud_operations():
    repo = InMemoryIncidentRepository()
    incident = Incident("I001", "Phishing Attack", "Email compromise", "High")

    repo.save(incident)
    assert repo.find_by_id("I001")._title == "Phishing Attack"
    assert len(repo.find_all()) == 1

    repo.delete("I001")
    assert repo.find_by_id("I001") is None
