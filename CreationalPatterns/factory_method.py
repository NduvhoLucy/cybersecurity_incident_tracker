class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        raise NotImplementedError()

class EmailNotification(Notification):
    def send(self):
        return f"Email sent to {self.recipient}: {self.message}"

class SMSNotification(Notification):
    def send(self):
        return f"SMS sent to {self.recipient}: {self.message}"

class NotificationFactory:
    @staticmethod
    def create_notification(channel, recipient, message):
        if channel == "email":
            return EmailNotification(recipient, message)
        elif channel == "sms":
            return SMSNotification(recipient, message)
        else:
            raise ValueError("Unsupported notification channel")
