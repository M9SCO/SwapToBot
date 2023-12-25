from aiogram import types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command

from bot import dp, bot
from swap import swap


@dp.message(Command("swap"))
async def swap_handler(message: types.Message) -> types.Message:
    if message.reply_to_message:
        text = message.reply_to_message.text
    elif not message.text.split(" ", 1)[-1].startswith("/swap"):
        text = message.text.split(" ", 1)[-1]
    else:
        try:
            getting_last_message = await bot.send_message(
                message.chat.id,
                "Получаю предыдущее сообщение...",
                reply_to_message_id=message.message_id - 1,
                disable_notification=True
            )
            text = getting_last_message.reply_to_message.text
        except TelegramBadRequest:
            return await message.answer(
                text="Не удалось получить сообщение для обработки, пожалуйста, выделите его")

    return await message.answer(swap(text))
