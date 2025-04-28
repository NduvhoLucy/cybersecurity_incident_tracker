from repositories.user_repository import UserRepository
from src.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage = {}

    def save(self, user: User) -> None:
        self._storage[user._user_id] = user

    def find_by_id(self, user_id: str) -> User:
        return self._storage.get(user_id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, user_id: str) -> None:
        if user_id in self._storage:
            del self._storage[user_id]
