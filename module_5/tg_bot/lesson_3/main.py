import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.webhook import PromoteChatMember
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
users = [629369830, 1863104264, 640639308, 1863104264, 1806940376, 5238737224, 1863104264, 1863104264, 1863104264, 5238737224, 1863104264, 5698317332, 5795085191, 1863104264, 5698317332, 1863104264, 5698317332, 1863104264, 1863104264, 5698317332, 1863104264, 5698317332, 5238737224, 5732085624, 1526992254]
users = set(users)


# @dp.message_handler()
# async def any_message(msg: types.Message):
#     print(msg.chat.id)


# @dp.message_handler(commands="count")
# async def any_message(msg: types.Message):
#     mkb = ReplyKeyboardMarkup(resize_keyboard=True)
#     # mkb.add(KeyboardButton("Location" , request_location=True))
#     # mkb.add(KeyboardButton("Phone" , request_contact=True))
#     mkb.add("btn1")
#     count = await bot.get_chat_members_count(msg.chat.id)
#     await msg.answer(count, reply_markup=mkb)










if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# {"message_id": 8,
#  "from": {"id": 1148477816,
#           "is_bot": false,
#           "first_name": "🟢//",
#           "last_name": "Абсаитов.Д.У",
#           "username": "Dilshod_Absaitov",
#           "language_code": "en"},
#  "chat": {"id": -1001733929545,
#           "title": "test2", "type": "supergroup"},
#  "date": 1692161843,
#  "text": "ds"}
#
# # {"message_id": 10,
# #  "from": {"id": 1148477816,
#           "is_bot": false,
#           "first_name": "🟢//",
#           "last_name": "Абсаитов.Д.У",
#           "username": "Dilshod_Absaitov",
#           "language_code": "en"},
#  "chat": {"id": -1001733929545,
#           "title": "test2",
#           "type": "supergroup"},
#  "date": 1692161937,
#  "message_thread_id": 5,
#  "reply_to_message": {"message_id": 5,
#                       "from": {"id": 6619757261,
#                                "is_bot": true,
#                                "first_name": "Botirjon Bot",
#                                "username": "Botirjon3234_bot"},
#                       "chat": {"id": -1001733929545,
#                                "title": "test2",
#                                "type": "supergroup"},
#                       "date": 1692161813,
#                       "text": "dsf"},
#  "text": "fdsgd"}
