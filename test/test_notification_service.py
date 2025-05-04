import unittest
from services.notification_service import NotificationService
from repositories.inmemory.notification_repository import InMemoryNotificationRepository
from models.notification import Notification

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryNotificationRepository()
        self.service = NotificationService(self.repository)

    def test_send_notification(self):
        notification = Notification(notification_id="N001", message="Test Alert", recipient="admin")
        self.service.send_notification(notification)
        self.assertEqual(self.service.get_notification("N001").message, "Test Alert")

if __name__ == "__main__":
    unittest.main()
