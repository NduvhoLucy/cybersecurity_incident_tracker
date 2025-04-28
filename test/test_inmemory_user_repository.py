from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from src.user import User

def test_user_crud_operations():
    repo = InMemoryUserRepository()
    user = User("U001", "Alice", "alice@example.com", "Analyst")

    repo.save(user)
    assert repo.find_by_id("U001")._name == "Alice"
    assert len(repo.find_all()) == 1

    repo.delete("U001")
    assert repo.find_by_id("U001") is None
