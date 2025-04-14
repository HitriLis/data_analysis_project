from typing import Optional
from db.interfaces import IDatabaseService
from schemas.login_request import LoginResponse


class LoginService:
    def __init__(self, db_service: IDatabaseService):
        self.db_service = db_service

    def check_login(self, guid: str, outer_ip: str, ng_token: str) -> Optional[LoginResponse]:
        query = """
            SELECT
                max(OuterIP = %(outer_ip)s) AS ip_seen,
                max(NgToken = %(ng_token)s) AS token_seen,
                count() AS user_exists
            FROM logins
            WHERE GUID = %(guid)s
        """
        params = {
            "guid": guid,
            "outer_ip": outer_ip,
            "ng_token": ng_token
        }
        result = self.db_service.client.query(query, params).result_rows
        if result and result[0][2] > 0:
            ip_seen, token_seen, _ = result[0]
            return LoginResponse(new_token=bool(token_seen), new_ip=bool(ip_seen))
