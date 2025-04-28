from repositories.notification_repository import NotificationRepository
from src.notification import Notification

class InMemoryNotificationRepository(NotificationRepository):
    def __init__(self):
        self._storage = {}

    def save(self, notification: Notification) -> None:
        self._storage[notification._notification_id] = notification

    def find_by_id(self, notification_id: str) -> Notification:
        return self._storage.get(notification_id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, notification_id: str) -> None:
        if notification_id in self._storage:
            del self._storage[notification_id]
