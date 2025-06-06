# Юзер-бот

## Описание

Простой юзер-бот для более удобного пользования телеграмом.
Позволяет добавлять цели для слежения времени и автоматически менять сообщения с временем.

## Команды

- `!ping` - проверить работоспособность бота
- `!id` - узнать ID чата или сообщения (ответом на сообщение)
- `!new_goal <time_in_iso> <goal_name>` - добавить новую цель для слежения времени
- `!goals` - получить все цели для слежения времени
- `!force_new_goal <goal_name> <chat_id> <message_id> <time_in_iso>` - добавить новую цель для слежения времени с указанием чата и сообщения
- `!delete_all_goals` - удалить все цели для слежения времени
- `!repeat <time in *h/*m/*s> <message>` - повторить сообщение через указанное время
- `!disable_repeat <repeat_id>` - отключить повторение сообщения
- `!repeats` - получить все активные повторения

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

## Миграции базы данных

Для работы с миграциями используется [Aerich](https://github.com/tortoise/aerich).

### Создание миграции

```bash
poetry run aerich migrate --name <migration_name>
```

### Применение миграций

```bash
poetry run aerich upgrade
```

### Откат миграции

```bash
poetry run aerich downgrade
```

### Просмотр статуса миграций

```bash
poetry run aerich history
```

### Просмотр текущей версии

```bash
poetry run aerich heads
```
