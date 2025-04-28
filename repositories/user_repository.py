from repositories.repository import Repository
from src.user import User

class UserRepository(Repository[User, str]):
    pass
