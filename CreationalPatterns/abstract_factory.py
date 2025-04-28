class UIComponent:
    def render(self):
        raise NotImplementedError()

class AdminDashboard(UIComponent):
    def render(self):
        return "Admin Dashboard Rendered"

class AnalystDashboard(UIComponent):
    def render(self):
        return "Analyst Dashboard Rendered"

class RoleUIFactory:
    @staticmethod
    def get_dashboard(role):
        if role == "admin":
            return AdminDashboard()
        elif role == "analyst":
            return AnalystDashboard()
        else:
            raise ValueError("Unknown role")
