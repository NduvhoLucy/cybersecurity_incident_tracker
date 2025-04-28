from repositories.repository import Repository
from src.incident import Incident

class IncidentRepository(Repository[Incident, str]):
    pass
