# Bot token can be obtained via https://t.me/BotFather
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

TOKEN = getenv("BOT_TOKEN")
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()