from repositories.case_repository import CaseRepository
from src.case import Case

class InMemoryCaseRepository(CaseRepository):
    def __init__(self):
        self._storage = {}

    def save(self, case: Case) -> None:
        self._storage[case._case_id] = case

    def find_by_id(self, case_id: str) -> Case:
        return self._storage.get(case_id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, case_id: str) -> None:
        if case_id in self._storage:
            del self._storage[case_id]
