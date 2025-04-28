from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from repositories.inmemory.inmemory_case_repository import InMemoryCaseRepository
from repositories.inmemory.inmemory_audit_log_repository import InMemoryAuditLogRepository
from repositories.inmemory.inmemory_report_repository import InMemoryReportRepository
from repositories.inmemory.inmemory_notification_repository import InMemoryNotificationRepository

# (Optional future imports if you add database storage)
# from repositories.database.database_user_repository import DatabaseUserRepository

class RepositoryFactory:
    @staticmethod
    def get_user_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryUserRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_incident_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryIncidentRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_case_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryCaseRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_audit_log_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryAuditLogRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_report_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryReportRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_notification_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryNotificationRepository()
        else:
            raise ValueError("Unsupported storage type")
