import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.webhook import PromoteChatMember
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
datas = [
    {
    "msg": "salom",
     "reply_msg": "Hi"}
]

@dp.message_handler(commands="datas")
async def any_message(msg: types.Message):
    await msg.answer(f"{datas}")
@dp.message_handler()
async def any_message(msg: types.Message):
    l = []
    for i in datas:
        if msg.text == i.get("msg"):
            l.append(i.get("reply_msg"))


    if not l:
        if msg.reply_to_message:

            data = {
                "msg": msg.reply_to_message.text,
                "reply_msg": msg.text
            }
            datas.append(data)
    else:
        await msg.reply(l[-1])







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
