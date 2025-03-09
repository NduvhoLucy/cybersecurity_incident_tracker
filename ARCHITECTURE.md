# Cybersecurity Incident Tracker - Architecture Model

## 1. System Overview
The **Cybersecurity Incident Tracker** follows a **three-tier architecture**:
- **Frontend:** Web-based user interface.
- **Backend:** API server for handling incidents.
- **Database:** Stores all security events.

## 2. C4 Architectural Diagrams

### **Context Diagram**
```mermaid
C4Context
    title Cybersecurity Incident Tracker Context
    Person(User, "Security Analyst", "Manages security incidents")
    System(System, "Cybersecurity Incident Tracker", "Logs and tracks security incidents")
    System_Ext(SIEM, "Security Information & Event Management (SIEM)", "Generates security alerts")
    
    User -> System : Reports and tracks incidents
    SIEM -> System : Sends security alerts

C4Container
    title Cybersecurity Incident Tracker Containers
    Person(User, "Security Analyst", "Uses the system to track incidents")
    
    System_Boundary(System, "Cybersecurity Incident Tracker") {
        Container(WebApp, "Web Application", "React.js / Angular", "Frontend UI for security analysts")
        Container(API, "Backend API", "Node.js / Django", "Handles incident management logic")
        ContainerDB(Database, "Incident Database", "PostgreSQL / MongoDB", "Stores incident logs")
    }
    
    User -> WebApp : Logs in and manages incidents
    WebApp -> API : Sends/receives incident data
    API -> Database : Stores and retrieves incident logs

C4Component
    title Cybersecurity Incident Tracker Components
    
    Container_Boundary(API, "Backend API") {
        Component(IncidentService, "Incident Service", "Manages incident lifecycle")
        Component(UserAuth, "User Authentication", "Handles login & roles")
        Component(Reporting, "Incident Reporting", "Generates audit reports")
    }
    
    IncidentService -> Database : Stores incident data
    UserAuth -> Database : Manages users & authentication
    Reporting -> Database : Retrieves incident history
```
