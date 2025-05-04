from fastapi import APIRouter
from services.notification_service import NotificationService
from models.notification import Notification
from typing import List

router = APIRouter()
notification_service = NotificationService()

@router.get("/api/notifications", response_model=List[Notification])
def get_all_notifications():
    return notification_service.get_all_notifications()

@router.post("/api/notifications")
def send_notification(notification: Notification):
    notification_service.send_notification(notification)
    return {"message": "Notification sent"}