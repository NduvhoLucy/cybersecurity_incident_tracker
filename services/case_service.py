from repositories.inmemory.case_inmemory_repository import InMemoryCaseRepository
from src.case import Case

class CaseService:
    def __init__(self, repository=None):
        self.repository = repository or InMemoryCaseRepository()

    def create_case(self, case: Case):
        if not case.id or not case.incident_id:
            raise ValueError("Case must have an ID and associated incident ID.")
        self.repository.save(case)

    def get_case(self, case_id: str):
        return self.repository.find_by_id(case_id)

    def list_all_cases(self):
        return self.repository.find_all()

    def delete_case(self, case_id: str):
        self.repository.delete(case_id)
