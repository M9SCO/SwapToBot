import asyncio
import logging
import sys

from aiogram import Bot, types
from aiogram.enums import ParseMode

from bot import dp, TOKEN, bot
from commands.start_handler import start_handler
from commands.swap_handler import swap_handler

__all__ = [
    "start_handler",
    "swap_handler",
]


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
