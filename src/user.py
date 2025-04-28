class User:
    def __init__(self, user_id, name, email, role, status="Pending"):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._role = role
        self._status = status

    def login(self):
        return f"{self._name} logged in."

    def logout(self):
        return f"{self._name} logged out."

    def request_access(self):
        return f"{self._name} requested access."