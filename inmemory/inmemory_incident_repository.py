from repositories.incident_repository import IncidentRepository
from src.incident import Incident

class InMemoryIncidentRepository(IncidentRepository):
    def __init__(self):
        self._storage = {}

    def save(self, incident: Incident) -> None:
        self._storage[incident._incident_id] = incident

    def find_by_id(self, incident_id: str) -> Incident:
        return self._storage.get(incident_id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, incident_id: str) -> None:
        if incident_id in self._storage:
            del self._storage[incident_id]
