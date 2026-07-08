"""
Aggregates all v1 route modules. Each future take (auth, datasets, KPIs,
dashboards, reports...) adds its own router module here — never add routes
directly in main.py.
"""
from fastapi import APIRouter

from app.api.v1.health import router as health_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router, tags=["system"])
