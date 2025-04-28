class SIEMConnection:
    _instance = None

    def __new__(cls, tool_name="Default SIEM"):
        if cls._instance is None:
            cls._instance = super(SIEMConnection, cls).__new__(cls)
            cls._instance.tool_name = tool_name
        return cls._instance

    def connect(self):
        return f"Connected to {self.tool_name}"
