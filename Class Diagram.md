classDiagram
    class User {
        -userId: String
        -name: String
        -email: String
        -role: String
        -status: String
        +login()
        +logout()
        +requestAccess()
    }

    class Incident {
        -incidentId: String
        -title: String
        -description: String
        -severity: String
        -status: String
        -createdAt: Date
        -updatedAt: Date
        +createIncident()
        +updateStatus()
        +escalateIncident()
        +closeIncident()
    }

    class Case {
        -caseId: String
        -incidentId: String
        -analystId: String
        -status: String
        -notes: String
        +assignToAnalyst()
        +addNote()
        +closeCase()
    }

    class AuditLog {
        -logId: String
        -timestamp: Date
        -action: String
        -actorId: String
        +recordAction()
        +exportLog()
    }

    class Report {
        -reportId: String
        -type: String
        -createdBy: String
        -createdAt: Date
        -content: String
        +generateReport()
        +exportPDF()
    }

    class SIEMIntegration {
        -integrationId: String
        -toolName: String
        -status: String
        -lastSync: Date
        +connect()
        +sendEvent()
        +retrySync()
    }

    class Notification {
        -notificationId: String
        -type: String
        -recipientId: String
        -message: String
        -status: String
        +sendNotification()
        +markAsRead()
    }

    User "1" -- "0..*" Incident : creates
    User "1" -- "0..*" Case : manages
    User "1" -- "0..*" AuditLog : performs
    User "1" -- "0..*" Report : generates

    Incident "1" -- "1" Case : linked to
    Incident "1" -- "0..*" Notification : triggers
    Case "1" -- "0..*" Notification : notifies

    SIEMIntegration "1" -- "0..*" Incident : sends
    SIEMIntegration "1" -- "0..*" AuditLog : logs
