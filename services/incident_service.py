from repositories.inmemory.incident_inmemory_repository import InMemoryIncidentRepository
from src.incident import Incident

class IncidentService:
    def __init__(self, repository=None):
        self.repository = repository or InMemoryIncidentRepository()

    def log_incident(self, incident: Incident):
        if not incident.id or not incident.description:
            raise ValueError("Incident must have an ID and description.")
        self.repository.save(incident)

    def get_incident(self, incident_id: str):
        return self.repository.find_by_id(incident_id)

    def list_all_incidents(self):
        return self.repository.find_all()

    def delete_incident(self, incident_id: str):
        self.repository.delete(incident_id)
