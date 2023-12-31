import logging
import asyncio
import sys

from aiogram.filters.command import Command

from loader import dp, bot, bot_db, db_users
import handlers
from handlers.users.dynamic_test import init_questions

@dp.startup()
async def on_startup(dispatcher):
    bot_db.open()
    db_users.connect(bot_db)
    db_users.create_default_tables()

    init_questions()
    logging.info("Bot has runned")

@dp.shutdown()
async def on_shutdown(dispatcher):
    bot_db.close()
    logging.info("Bot has stopped")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
