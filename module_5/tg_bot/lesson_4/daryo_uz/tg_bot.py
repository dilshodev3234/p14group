import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.webhook import PromoteChatMember
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from module_5.tg_bot.lesson_4.daryo_uz.main import news_data

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="news")
async def any_message(msg: types.Message):
    datas = news_data()
    for i in datas:
        text = f"""
{i.get('title')}

{i.get('date')}

[Daryo Uz](https://t.me/daryo_3234)
        """
        await msg.bot.send_photo(-1001842354993 , f"https://daryo.uz/{i.get('photo_link')}",caption=text,parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
