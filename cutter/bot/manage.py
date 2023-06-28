
import logging
import asyncio

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

import requests
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


# def wrap_media(bytesio, **kwargs):
#     """Wraps plain BytesIO objects into InputMediaPhoto"""
#     # First, rewind internal file pointer to the beginning so the contents
#     #  can be read by InputFile class
#     bytesio.seek(0)
#     return types.InputMediaPhoto(types.InputFile(bytesio), **kwargs)

@dp.message(F.text)
async def get_url(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Сгенерировать qr код",
        callback_data="generate_qr")
    )
    if is_string_an_url(message.text):
        response = requests.post(
            "http://127.0.0.1:50800/url/", data={'url': message.text}
        )
        data = response.json()
        await message.answer(data)

        await bot.send_photo(chat_id=message.from_user.id, photo=generate_qr(data))
        # await message.answer(
        #     "Нажмите на кнопку, чтобы бот сгенерировал qr код",
        #     reply_markup=builder.as_markup()
        # )
    else:
        await message.reply("Только ссылки")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())