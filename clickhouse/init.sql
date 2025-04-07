-- Создание базы данных (если она не существует)
CREATE DATABASE IF NOT EXISTS analysis;

-- Переключаемся на созданную базу данных
USE analysis;

-- Создание таблицы для пользователей
CREATE TABLE IF NOT EXISTS user_info
(
    GUID String,
    LastName String,
    FirstName String,
    MiddleName String
)
ENGINE = MergeTree()
ORDER BY GUID;

-- Создание таблицы для логинов
CREATE TABLE IF NOT EXISTS logins
(
    Timestamp DateTime,
    GUID String,
    OuterIP String,
    InnerIP String,
    OpenVPNServer String,
    NgToken String
)
ENGINE = MergeTree()
ORDER BY Timestamp;