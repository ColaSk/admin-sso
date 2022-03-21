from typing import Any, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from apps.extensions.route import LoggingRoute

router = APIRouter(route_class=LoggingRoute)

class TestRequest(BaseModel):
    name: str

@router.get('/login', status_code=200)
def test():
    return ""