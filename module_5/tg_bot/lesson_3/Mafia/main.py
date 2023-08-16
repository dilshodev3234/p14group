import logging
from _socket import timeout
from datetime import timedelta
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.webhook import PromoteChatMember
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ChatPermissions, InlineKeyboardMarkup, \
    InlineKeyboardButton

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
role = ["Mafia" , "Tinch axoli" , "Kamissar"]
user_data = dict(
)

@dp.message_handler(commands="game")
async def register_user(msg: types.Message):
    inb = InlineKeyboardButton("👨🏻‍💻 qo'shilish", callback_data="add")
    ikm = InlineKeyboardMarkup()
    ikm.add(inb)

    await msg.answer("*Ro'yhatdan o'tish boshladi*" ,reply_markup=ikm, parse_mode="Markdown")



@dp.callback_query_handler(Text("add"))
async def add_users(callback : types.CallbackQuery):
    inb = InlineKeyboardButton("👨🏻‍💻 qo'shilish", callback_data="add")
    ikm = InlineKeyboardMarkup()
    ikm.add(inb)

    data = dict(callback.from_user)
    print(data)
    user_data[callback.from_user.id] = data

    text = f"*Ro'yhatdan o'tgalar ({len(user_data)})*: \n"
    for v in user_data.values():
        text += f"[{v.get('first_name')} {v.get('last_name')}](https://t.me/{v.get('username')})  ,  "
    await callback.message.edit_text(text , reply_markup=ikm, parse_mode="Markdown")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
