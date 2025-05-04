from fastapi import APIRouter, HTTPException
from typing import List
from services.report_service import ReportService
from src.report import Report

router = APIRouter(prefix="/api/reports")
report_service = ReportService()

@router.get("/", response_model=List[Report])
def get_all_reports():
    return report_service.get_all()

@router.post("/", response_model=Report)
def create_report(report: Report):
    return report_service.create(report)

@router.put("/{report_id}", response_model=Report)
def update_report(report_id: str, report: Report):
    try:
        return report_service.update(report_id, report)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
yes