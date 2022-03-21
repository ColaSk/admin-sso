from typing import Any, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class TestRequest(BaseModel):
    name: str

@router.post('/login', status_code=200)
def test(body: TestRequest):
    return body