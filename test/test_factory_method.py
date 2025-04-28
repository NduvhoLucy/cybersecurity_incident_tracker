from creational_patterns.factory_method import NotificationFactory

def test_create_email_notification():
    notification = NotificationFactory.create_notification("email", "user@example.com", "Security Alert")
    result = notification.send()
    assert result == "Email sent to user@example.com: Security Alert"

def test_create_sms_notification():
    notification = NotificationFactory.create_notification("sms", "+123456789", "Security Alert")
    result = notification.send()
    assert result == "SMS sent to +123456789: Security Alert"
