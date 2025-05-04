from fastapi import APIRouter, HTTPException
from services.incident_service import IncidentService
from models.incident import Incident
from typing import List

router = APIRouter()
incident_service = IncidentService()

@router.get("/api/incidents", response_model=List[Incident])
def get_all_incidents():
    return incident_service.get_all_incidents()

@router.post("/api/incidents")
def create_incident(incident: Incident):
    incident_service.create_incident(incident)
    return {"message": "Incident created successfully"}