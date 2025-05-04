from fastapi import APIRouter
from services.audit_log_service import AuditLogService
from models.audit_log import AuditLog
from typing import List

router = APIRouter()
audit_log_service = AuditLogService()

@router.get("/api/auditlogs", response_model=List[AuditLog])
def get_all_audit_logs():
    return audit_log_service.get_all_logs()