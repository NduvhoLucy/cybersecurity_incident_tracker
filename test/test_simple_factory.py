from creational_patterns.simple_factory import ObjectFactory

def test_create_incident():
    incident = ObjectFactory.create_object("incident", "Phishing Attack")
    assert incident.title == "Phishing Attack"

def test_create_report():
    report = ObjectFactory.create_object("report", "Weekly Summary")
    assert report.report_name == "Weekly Summary"
