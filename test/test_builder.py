from creational_patterns.builder import ReportBuilder

def test_build_report():
    builder = ReportBuilder()
    report = builder.set_title("Incident Report").set_content("Incident details...").set_created_by("SOC Manager").build()
    assert report.title == "Incident Report"
    assert report.content == "Incident details..."
    assert report.created_by == "SOC Manager"
