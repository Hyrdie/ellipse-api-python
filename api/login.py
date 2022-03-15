from typing import Optional
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi import status, Form, Depends
from fastapi.security import OAuth2PasswordRequestForm

from service.login import login

login_router = InferringRouter()

def make_response(payload: dict = {}, message: str = 'success', meta: dict = {}, code: int = 200):
        return JSONResponse(status_code=code, content={"message": message, "meta":meta, "data": payload})

@login_router.post("/login")
def post_login(username: str = Form(...), password: str = Form(...), position: str = Form(...), district: str = Form(...)):
    result = login(username, password, position, district)
    if result[0] is None:
        return make_response(message="success", payload={"username": username, "position": result[1], "district": result[2]},
                              code=200)
    if "fault" in result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=result)
