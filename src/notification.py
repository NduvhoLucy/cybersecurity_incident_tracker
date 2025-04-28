class Notification:
    def __init__(self, notification_id, type_, recipient_id, message, status="Created"):
        self._notification_id = notification_id
        self._type = type_
        self._recipient_id = recipient_id
        self._message = message
        self._status = status

    def send_notification(self):
        self._status = "Delivered"
        return f"Notification {self._notification_id} sent to {self._recipient_id}."

    def mark_as_read(self):
        self._status = "Acknowledged"
        return f"Notification {self._notification_id} marked as read."