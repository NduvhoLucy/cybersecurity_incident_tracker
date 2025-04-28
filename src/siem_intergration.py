class SIEMIntegration:
    def __init__(self, integration_id, tool_name, status="Configuring", last_sync=None):
        self._integration_id = integration_id
        self._tool_name = tool_name
        self._status = status
        self._last_sync = last_sync

    def connect(self):
        self._status = "Active"
        return f"Connected to SIEM tool {self._tool_name}."

    def send_event(self, event):
        return f"Event sent to SIEM: {event}"

    def retry_sync(self):
        return "Retrying SIEM synchronization..."