from repositories.inmemory.notification_inmemory_repository import InMemoryNotificationRepository
from src.notification import Notification

class NotificationService:
    def __init__(self, repository=None):
        self.repository = repository or InMemoryNotificationRepository()

    def send_notification(self, notification: Notification):
        if not notification.id or not notification.message:
            raise ValueError("Notification must have an ID and a message.")
        self.repository.save(notification)

    def get_notification(self, notification_id: str):
        return self.repository.find_by_id(notification_id)

    def list_all_notifications(self):
        return self.repository.find_all()

    def delete_notification(self, notification_id: str):
        self.repository.delete(notification_id)
