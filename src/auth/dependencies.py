from fastapi.security import HTTPBearer
from fastapi import Request
from fastapi.security.http import HTTPAuthorizationCredentials

class AccessJWTBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None :
        creds =  await super().__call__(request)
        print(creds.scheme)
        print(creds.credentials)
        return creds