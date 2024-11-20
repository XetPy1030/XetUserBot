# Юзер-бот

## Описание

Простой юзер-бот для более удобного пользования телеграмом.
Позволяет добавлять цели для слежения времени и автоматически менять сообщения с временем.

## Команды

- `/id` - узнать ID чата или сообщения (ответом на сообщение)
- `/new_goal <time_in_iso> <goal_name>` - добавить новую цель для слежения времени
- `/goals` - получить все цели для слежения времени
- `/force_new_goal <goal_name> <chat_id> <message_id> <time_in_iso>` - добавить новую цель для слежения времени с указанием чата и сообщения
- `/delete_all_goals` - удалить все цели для слежения времени

## Установка

1. Установить зависимости
```bash
pip install poetry
poetry install
```

2. Создать файл `.env` и добавить туда переменные окружения
```bash
API_ID=123
API_HASH=123
PHONE_NUMBER=123
TELEGRAM_PASSWORD=123
```

3. Сконфигурировать `configure_sessions.py` и запустить его
```bash
poetry run python configure_sessions.py
```

4. Запустить docker-compose
```bash
docker compose up -d
```
