import unittest
from services.case_service import CaseService
from repositories.inmemory.case_repository import InMemoryCaseRepository
from models.case import Case

class TestCaseService(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryCaseRepository()
        self.service = CaseService(self.repository)

    def test_assign_case(self):
        case = Case(case_id="C001", incident_id="I001", assigned_to="admin")
        self.service.assign_case(case)
        self.assertEqual(self.service.get_case("C001").assigned_to, "admin")

    def test_close_case(self):
        case = Case(case_id="C002", incident_id="I002", assigned_to="analyst")
        self.service.assign_case(case)
        self.service.close_case("C002")
        self.assertEqual(self.service.get_case("C002").status, "Closed")

if __name__ == "__main__":
    unittest.main()
