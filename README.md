# 🚀 Swipe Service

## 📋 Описание

Асинхронный микросервис, для обработки свайпов в системе знакомств. Сервис получает
события через Apache Kafka, обрабатывает их асинхронно и сохраняет результаты в базе
данных PostgreSQL.

## 🛠️ Технологический стек

- **Python 3.12** — основной язык разработки
- **FastAPI** — современный асинхронный web-фреймворк
- **SQLAlchemy** — ORM для работы с базой данных
- **Alembic** — миграции схемы БД
- **PostgreSQL** — реляционная база данных
- **Kafka (aiokafka)** — брокер сообщений для асинхронной обработки событий
- **Docker, docker-compose** — контейнеризация и оркестрация сервисов
- **Poetry** — управление зависимостями и пакетами
- **Pydantic** — валидация и сериализация данных
- **ruff** — быстрый и современный линтер для Python

## 🏗️ Архитектура

Проект следует принципам Clean Architecture с четким разделением слоев:

```
src/
├── config/           # Конфигурация приложения
│   ├── broker/      # Настройки Kafka
│   └── database/    # Настройки базы данных
├── models/          # SQLAlchemy модели
├── swipe/           # Основная бизнес-логика
│   ├── adapters/    # Адаптеры (Kafka Consumer)
│   ├── controllers/ # HTTP контроллеры
│   ├── dependencies/# Dependency injection
│   ├── exceptions/  # Кастомные исключения
│   ├── repositories/# Слой доступа к данным
│   ├── schemas/     # Pydantic схемы
│   └── services/    # Бизнес-логика
└── main.py         # Точка входа приложения
```

## 🚀 Быстрый старт

### Развертывание с помощью Docker

1. Создайте папку с проектом и склонируйте репозиторий:

```bash
mkdir swipe_service
cd swipe_service
git clone https://github.com/aquaracer/Fastapi-Swipe-Microservice.git
```

2. Настройте переменные окружения в файле .env.

3. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```

4. Примените миграции базы данных:

```bash
docker exec -it swipe_service bash
poetry run alembic upgrade head
```

Приложение будет доступно по следующим адресам:

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
