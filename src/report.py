class Report:
    def __init__(self, report_id, type_, created_by, created_at, content):
        self._report_id = report_id
        self._type = type_
        self._created_by = created_by
        self._created_at = created_at
        self._content = content

    def generate_report(self):
        return f"Report {self._report_id} generated."

    def export_pdf(self):
        return f"Report {self._report_id} exported as PDF."
