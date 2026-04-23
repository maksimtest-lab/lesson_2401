# lesson_2401

## Задание

Погода. Разработайте бота, который позволяет пользователям получать текущую погоду в определенном городе по запросу.

## Установка Python 3.11

Я столкнулся с пролемой работы в 3.14, поэтому использую 3.11.

```bash
uv python install 3.11
uv venv --python 3.11 .venv311
source .venv311/bin/activate.fish
uv pip install -r requirements.txt
```

## Секреты
Хранятся в файле `.env` или в переменных окружения

```bash
export TELEGRAM_BOT_TOKEN="your_token_here"
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Запуск

```bash
source .venv311/bin/activate.fish
python weather_bot.py
```