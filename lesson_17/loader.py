from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data import config
from utils.db_api import BotDb, DbUsers

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

bot_db = BotDb(config.DB_FILE)
db_users = DbUsers()

ques = {
        1: {
            "question":"What time is it",
            "level": "A1",
            "translation":"Котра година",
            "answers":"Yellow@It's 2 o'clock@Number3",
            "right_answer": "It's 2 o'clock",
            "point": 1
        },
        2: {
            "question":"What time is it",
            "level": "A1",
            "translation":"Котра година",
            "answers":"Yellow@It's 2 o'clock@Number3",
            "right_answer": "It's 2 o'clock",
            "point": 1
        },
        3: {
            "question":"What time is it",
            "level": "A1",
            "translation":"Котра година",
            "answers":"Yellow@It's 2 o'clock@Number3",
            "right_answer": "It's 2 o'clock",
            "point": 1
        }
    }