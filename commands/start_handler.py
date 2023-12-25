from aiogram import types
from aiogram.filters import CommandStart, Command

from bot import dp


@dp.message(CommandStart())
@dp.message(Command("help"))
async def start_handler(message: types.Message) -> types.Message:
    return await message.reply(f"Привет, {message.from_user.full_name}! Я бот, выполняющий одну простую задачу -- "
                                f"перевожу любой текст с забытой раскладки в правильную. Например:\n"
                               f"\"ghbdtn\" → \"привет\"\n"
                               f"Мои исходники можно найти на гитхабе: ")

