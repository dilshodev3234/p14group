from aiogram import Bot , Dispatcher , types , executor
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.types import ReplyKeyboardMarkup

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# class MyFilter(Filter):
#     def __init__(self, message_text):
#         self.message_text = message_text
#
#     async def check(self, *args) -> bool:
#         pass
#
#     def __invert__(self):
#         return super().__invert__()
#
#     def __and__(self, other):
#         return super().__and__(other)
#
#     def __or__(self, other):
#         return super().__or__(other)
#
#     async def __call__(self, message):
#         return self.message_text == message.text

#
# @dp.message_handler(commands='start')
# async def start_handler(message: types.Message):
#
#     text = f"https://t.me/Botirjon3234_bot?start={message.from_user.id}"
#     await message.answer(text)
#
# @dp.message_handler(commands=["lang" , "language"])
# async def language_handler(message: types.Message):
#
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add("🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG" , "🇺🇿UZB")
#     await message.answer("Choice language 👇🏿", reply_markup=markup)


# @dp.message_handler(lambda msg: msg.text in ("🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG" , "🇺🇿UZB"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")
#
# @dp.message_handler(Text("🇺🇿UZB"))
# @dp.message_handler(MyFilter("🇺🇿UZB"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")

# @dp.message_handler(lambda msg: msg.text.startswith("🇺🇿U") or msg.text.startswith("🏴󠁧󠁢󠁥󠁮󠁧󠁿E"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")

# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
# async def handler_phone(message: types.Message):
#     phone = message.contact.phone_number
#     await message.answer(phone)
#
# @dp.message_handler(content_types=types.ContentTypes.LOCATION)
# async def handler_phone(message: types.Message):
#     lat = message.location.latitude
#     long = message.location.longitude
#     await message.answer(f"{lat}:{long}")

# @dp.message_handler(lambda msg : len(msg.text.split()) == 2 , CommandStart())
# async def rental_chat_id(message: types.Message):
#     print(f"{message.from_user.id} {message.text.split()[-1]}")









# https://t.me/Botirjon3234_bot?start=10049























if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)


