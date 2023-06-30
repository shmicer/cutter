import base64

import requests
import logging
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import BufferedInputFile, InputFile
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from api.services import generate_qr
from config import API_TOKEN


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


def is_string_an_url(url):
    val = URLValidator()
    try:
        val(url)
    except ValidationError:
        return False
    return val


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='some_file.png'
    )
    await message.reply("Привет, я умею сокращать ссылки. Отправь мне ссылку и увидишь")


@dp.message(F.text)
async def get_url(message: types.Message):
    if is_string_an_url(message.text):
        response = requests.post(
            "http://127.0.0.1:50800/url/", data={'url': message.text}
        )
        data = response.json()
        photo = base64.b64decode(data['qr_code'])
        photo = BufferedInputFile(photo, "qrcode.png")
        await message.answer(data['short_link'])
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    else:
        await message.reply("Только ссылки")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
