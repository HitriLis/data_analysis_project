# Data Analysis Project

## Описание
Проект для анализа данных пользователей и логинов с использованием Jupyter Notebook, Docker и ClickHouse.

## Возможности
- [**API**](http://localhost:8000/docs) — Проверка на новый IP-адрес или NgToken для указанного пользователя..
- [**Jupyter Notebook**](http://localhost:8888/lab) — Работ с Jupyter Notebook.

## Установка
1. **Клонируйте репозиторий**:

    ```bash
    git clone https://github.com/HitriLis/data_analysis_project.git
    ```

2. **Перейдите в директорию проекта**:

    ```bash
    cd data_analysis_project
    ```
3. **Настройте переменные окружения**:

    - В корневой директории проекта уже есть файл `.env.example`.  
      Скопируйте его в `.env` и заполните своими данными:

      ```bash
      cp .env.example .env
      ```

    - Откройте `.env` и укажите нужные параметры:

      ```ini
      # Конфигурация базы данных
      CLICKHOUSE_USER=default
      CLICKHOUSE_PASSWORD=secret_password
      CLICKHOUSE_DB=analysis
      CLICKHOUSE_HOST=clickhouse
      CLICKHOUSE_PORT=8123
      ```

    ⚠️ **Важно!** Не загружайте `.env` в репозиторий — он уже добавлен в `.gitignore`.

## Docker

1. **Запустите приложение**:
    ```bash
    docker-compose up -d
    ```