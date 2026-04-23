import os
import aiohttp
from aiogram import Bot, Dispatcher, types, executor

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


async def get_weather(city: str):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            return await response.json()


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Напиши название города, и я покажу текущую погоду."
    )


@dp.message_handler()
async def weather_handler(message: types.Message):
    city = message.text.strip()

    data = await get_weather(city)

    if data is None or data.get("cod") != 200:
        await message.answer("Не удалось найти такой город. Попробуй другой.")
        return

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"].capitalize()

    text = (
        f"🌤 Погода в городе *{city.title()}*\n\n"
        f"Температура: {temp}°C\n"
        f"Ощущается как: {feels}°C\n"
        f"Влажность: {humidity}%\n"
        f"Описание: {desc}"
    )

    await message.answer(text, parse_mode="Markdown")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
