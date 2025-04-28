class Incident:
    def __init__(self, incident_id, title, description, severity, status="New", created_at=None, updated_at=None):
        self._incident_id = incident_id
        self._title = title
        self._description = description
        self._severity = severity
        self._status = status
        self._created_at = created_at
        self._updated_at = updated_at

    def create_incident(self):
        self._status = "New"
        return f"Incident {self._incident_id} created."

    def update_status(self, new_status):
        self._status = new_status
        return f"Incident {self._incident_id} status updated to {new_status}."

    def escalate_incident(self):
        self._severity = "High"
        self.update_status("Escalated")
        return "Incident escalated."

    def close_incident(self):
        self._status = "Closed"
        return f"Incident {self._incident_id} closed."