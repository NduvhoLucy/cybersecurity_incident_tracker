from fastapi import APIRouter, HTTPException
from services.case_service import CaseService
from models.case import Case
from typing import List

router = APIRouter()
case_service = CaseService()

@router.get("/api/cases", response_model=List[Case])
def get_all_cases():
    return case_service.get_all_cases()

@router.post("/api/cases")
def create_case(case: Case):
    case_service.create_case(case)
    return {"message": "Case created successfully"}