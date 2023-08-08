import asyncio
import base64

import logging

import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import BufferedInputFile

from os import getenv


API_TOKEN = getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='some_file.png'
    )
    await message.reply("Привет, я умею сокращать ссылки."
                        " Отправь мне ссылку и увидишь")


@dp.message(F.text)
async def get_url(message: types.Message):
    # if is_string_an_url(message.text):
    response = requests.post(
        "https://cl2u.ru/url", data={'url': message.text}
    )
    response.raise_for_status()
    data = response.json()
    photo = base64.b64decode(data['qr_code'])
    photo = BufferedInputFile(photo, "qrcode.png")
    await message.answer(f'Ссылка: \n {data["short_link"][8:]}')
    await message.answer('QR-code:')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    # else:
    #     await message.reply("Только ссылки")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
