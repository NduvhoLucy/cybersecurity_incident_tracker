from repositories.inmemory.inmemory_notification_repository import InMemoryNotificationRepository
from src.notification import Notification

def test_notification_crud_operations():
    repo = InMemoryNotificationRepository()
    notification = Notification("N001", "Email", "user123", "Security alert!")

    repo.save(notification)
    assert repo.find_by_id("N001")._message == "Security alert!"
    assert len(repo.find_all()) == 1

    repo.delete("N001")
    assert repo.find_by_id("N001") is None
