from typing import Any, Optional, Dict
from fastapi.exceptions import HTTPException

class NotFound(HTTPException):

    def __init__(
        self, 
        status_code: int = 404,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None):

        super().__init__(status_code, detail, headers)