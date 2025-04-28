class Report:
    def __init__(self):
        self.title = None
        self.content = None
        self.created_by = None

class ReportBuilder:
    def __init__(self):
        self._report = Report()

    def set_title(self, title):
        self._report.title = title
        return self

    def set_content(self, content):
        self._report.content = content
        return self

    def set_created_by(self, creator):
        self._report.created_by = creator
        return self

    def build(self):
        return self._report
