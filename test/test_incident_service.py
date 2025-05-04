import unittest
from services.incident_service import IncidentService
from repositories.inmemory.incident_repository import InMemoryIncidentRepository
from models.incident import Incident

class TestIncidentService(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryIncidentRepository()
        self.service = IncidentService(self.repository)

    def test_create_and_get_incident(self):
        incident = Incident(incident_id="I001", description="Phishing email")
        self.service.create_incident(incident)
        retrieved = self.service.get_incident("I001")
        self.assertEqual(retrieved.description, "Phishing email")

    def test_update_status(self):
        incident = Incident(incident_id="I002", description="Malware")
        self.service.create_incident(incident)
        self.service.update_status("I002", "Resolved")
        self.assertEqual(self.service.get_incident("I002").status, "Resolved")

if __name__ == "__main__":
    unittest.main()
