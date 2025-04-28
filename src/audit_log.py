class AuditLog:
    def __init__(self, log_id, timestamp, action, actor_id):
        self._log_id = log_id
        self._timestamp = timestamp
        self._action = action
        self._actor_id = actor_id

    def record_action(self):
        return f"Action {self._action} by {self._actor_id} recorded at {self._timestamp}."

    def export_log(self):
        return f"Exporting log {self._log_id}."
