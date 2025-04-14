from fastapi import APIRouter, HTTPException

from exceptions import ClickHouseConnectionError
from schemas.login_request import LoginRequest, LoginResponse
from dependencies.dependencies import GetLoginService

router = APIRouter()


@router.post("/check_login", response_model=LoginResponse)
def check_login(
        login: LoginRequest,
        login_service: GetLoginService
):
    try:
        response = login_service.check_login(
            guid=login.GUID,
            outer_ip=login.OuterIP,
            ng_token=login.NgToken
        )
        if response:
            return response
    except ClickHouseConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    raise HTTPException(status_code=404, detail='GUID Not Found')
