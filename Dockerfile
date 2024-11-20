FROM python:3.12-slim

WORKDIR /app

# Устанавливаем зависимости для системы (например, для Poetry и компиляции пакетов)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
ENV POETRY_VERSION=1.6.1
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Копируем файлы проекта в контейнер
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта
RUN poetry install --no-root --only main

# Копируем оставшиеся файлы проекта в контейнер
COPY . .

# Определяем команду по умолчанию для контейнера
CMD ["poetry", "run", "python", "main.py"]
