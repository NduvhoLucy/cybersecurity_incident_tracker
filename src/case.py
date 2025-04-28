class Case:
    def __init__(self, case_id, incident_id, analyst_id, status="Open", notes=""):
        self._case_id = case_id
        self._incident_id = incident_id
        self._analyst_id = analyst_id
        self._status = status
        self._notes = notes

    def assign_to_analyst(self, analyst_id):
        self._analyst_id = analyst_id
        self._status = "Assigned"
        return f"Case {self._case_id} assigned to analyst {analyst_id}."

    def add_note(self, note):
        self._notes += f"\n{note}"
        return "Note added to case."

    def close_case(self):
        self._status = "Closed"
        return f"Case {self._case_id} closed."
