import logging

from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart, CommandObject

from loader import db_users, dp

# user_flow_router = Router()

def format_user_info_string(user_info: tuple):
    return f"""
<b>
ID: {user_info[0]}
Username: {user_info[1]}
First Name: {user_info[2]}
Last Name: {user_info[3]}
Telegram ID: {user_info[4]}
</b>
"""



@dp.message(Command("get_user"))
async def get_user_by_id(msg: types.Message, command: CommandObject):
    try:
        # user_id = int(msg.text.split()[1])  # Отримання id з команди
        if command.args:
            user_id = int(command.args.split()[0])  # Отримання id з команди
            user_info = db_users.get_user_by_telegram_id(user_id)
            if user_info:
                await msg.reply(format_user_info_string(user_info))
            else:
                await msg.reply(f"User with your ID: <b>{user_id}</b> is not registred")
        else:
            await msg.reply("Usage: /getuser user_id")
    except (ValueError, IndexError):
        await msg.reply("Usage: /getuser user_id")


@dp.message(Command("get_me"))
async def get_user_by_id(msg: types.Message):
    user_id = msg.from_user.id
    fetch_result = db_users.get_user_by_telegram_id(user_id)
    if fetch_result:
        result = format_user_info_string(fetch_result)
    else:
        result = f"User with your ID: <b>{user_id}</b> is not registred"
    await msg.answer(result)


@dp.message(Command('add_user'))
async def add_user(msg: types.Message):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    username = msg.from_user.username

    if not db_users.user_exists(user_id):
        db_users.register_user(user_id, first_name, last_name, username)
        await msg.reply("User added successfully!")
    else:
        await msg.reply("User already exists.")


@dp.message(Command('delete_me'))
async def add_user(msg: types.Message):
    user_id = msg.from_user.id
    if db_users.user_exists(user_id):
        db_users.delete_user(user_id)
        await msg.reply("User deleted successfully!")
    else:
        await msg.reply("User not exists.")
