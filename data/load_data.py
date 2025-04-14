import os
import json
import logging
import time
from clickhouse_connect import get_client
import pandas as pd

logger = logging.getLogger('clickhouse_load_data')
logging.basicConfig(level=logging.INFO)


def wait_for_clickhouse():
    max_attempts = 10
    # Чтение параметров подключения
    CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST')
    CLICKHOUSE_PORT = int(os.getenv('CLICKHOUSE_PORT'))
    CLICKHOUSE_DB = os.getenv('CLICKHOUSE_DB')
    CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER')
    CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD')

    for i in range(max_attempts):
        try:
            client = get_client(
                host=CLICKHOUSE_HOST,
                port=CLICKHOUSE_PORT,
                database=CLICKHOUSE_DB,
                username=CLICKHOUSE_USER,
                password=CLICKHOUSE_PASSWORD
            )
            logger.info("Подключение к ClickHouse установлено!")
            return client
        except Exception as e:
            logger.info(f"Ожидание ClickHouse... Попытка {i + 1}/{max_attempts}, ошибка: {e}")
            time.sleep(2)


def load_logins(client_db):
    csv_path = "/home/jovyan/data/logins.csv"
    exists_logins = bool(client_db.query("SELECT 1 FROM logins LIMIT 1").result_rows)
    if exists_logins:
        logger.info("Данные уже есть в базе.")
        return
    if not os.path.isfile(csv_path):
        logger.info(f"Файл не найден: {csv_path}")
    else:
        try:
            # Читаем CSV с помощью pandas
            df = pd.read_csv(csv_path, parse_dates=['Timestamp'])
            if 'Unnamed: 0' in df.columns:
                df = df.drop(columns=['Unnamed: 0'])
            client_db.insert_df('logins', df)
            logger.info(f"Загружено {len(df)} записей в таблицу logins.")
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных: {e}")


def load_users(client_db):
    user_info_path = "/home/jovyan/data/user_info.json"
    exists_user = bool(client_db.query("SELECT 1 FROM user_info LIMIT 1").result_rows)
    if exists_user:
        logger.info("Данные уже есть в базе.")
        return
    if not os.path.isfile(user_info_path):
        logger.info(f"Файл не найден: {user_info_path}")
    else:
        with open(user_info_path, 'r', encoding='utf-8') as f:
            user_info_data = json.load(f)
        df = pd.DataFrame(user_info_data)
        if not df.empty:
            try:
                client_db.insert(
                    'user_info',
                    df
                )
                logger.info(f"Загружено {len(user_info_data)} записей в таблицу user_info.")
            except Exception as e:
                logger.info(f"Ошибка при загрузке user_info.json: {e}")
        else:
            logger.info("В файле нет данных для загрузки.")


if __name__ == "__main__":
    logger.info("Запуск скрипта загрузки данных...")
    client = wait_for_clickhouse()
    load_logins(client)
    load_users(client)
    logger.info("Скрипт завершил выполнение")
