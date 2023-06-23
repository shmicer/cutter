import logging
import os

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '6109151347:AAEXAV9qjQuRC7IVvTVDz7LrcBI96M4_B6c'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет, я умею сокращать ссылки. Отправь мне ссылку и увидишь")


def is_string_an_url(url: str) -> bool:
    val = URLValidator()
    try:
        val(url)
        return val
    except ValidationError:
        print("Только ссылки")


@dp.message_handler()
async def get_url(message: types.Message):
    if is_string_an_url(message.text):
        response = requests.post(
            "http://127.0.0.1:50800/url/", data={'url': message.text}
        )
        data = response.json()
        await message.answer(data)
    else:
        await message.reply("Только ссылки")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
