from typing import Annotated
from fastapi import Depends
from services.login_checker import LoginService
from utils.service import get_login_service

GetLoginService = Annotated[LoginService, Depends(get_login_service)]
