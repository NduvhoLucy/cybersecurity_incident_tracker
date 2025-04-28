from creational_patterns.abstract_factory import RoleUIFactory

def test_admin_dashboard():
    dashboard = RoleUIFactory.get_dashboard("admin")
    assert dashboard.render() == "Admin Dashboard Rendered"

def test_analyst_dashboard():
    dashboard = RoleUIFactory.get_dashboard("analyst")
    assert dashboard.render() == "Analyst Dashboard Rendered"
