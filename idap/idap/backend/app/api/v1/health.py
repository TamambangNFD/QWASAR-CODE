"""
Health check endpoint — used by Docker, load balancers, and CI to verify
the service is up. Extend this in later takes to check DB/Redis connectivity.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok", "service": "idap-backend"}
