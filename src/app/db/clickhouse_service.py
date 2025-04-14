import logging
from clickhouse_connect import get_client
from clickhouse_connect.driver.exceptions import ClickHouseError
import settings
from exceptions import ClickHouseConnectionError
from .interfaces import IDatabaseService

# Настройка логгера
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ClickHouseService(IDatabaseService):
    def __init__(self):
        self._client = None
        self._connect()

    def _connect(self):
        """Подключаемся к ClickHouse."""
        try:
            self._client = get_client(
                host=settings.CLICKHOUSE_HOST,
                port=settings.CLICKHOUSE_PORT,
                database=settings.CLICKHOUSE_DB,
                username=settings.CLICKHOUSE_USER,
                password=settings.CLICKHOUSE_PASSWORD
            )
            # Проверим подключение
            self._client.query("SELECT 1")
            logger.info("Подключение к ClickHouse успешно.")
        except Exception as e:
            logger.error(f"Ошибка подключения к ClickHouse: {e}")
            self._client = None
        except ClickHouseError as e:
            logger.error(f"ClickHouse ошибка: {e}")
            self._client = None

    @property
    def client(self):
        if not self._client:
            raise ClickHouseConnectionError("ClickHouse клиент не инициализирован.")
        return self._client
