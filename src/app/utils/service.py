from db.clickhouse_service import ClickHouseService
from services.login_checker import LoginService


def get_login_service() -> LoginService:
    clickhouse_service = ClickHouseService()
    return LoginService(db_service=clickhouse_service)