from repositories.repository import Repository
from src.notification import Notification

class NotificationRepository(Repository[Notification, str]):
    pass
