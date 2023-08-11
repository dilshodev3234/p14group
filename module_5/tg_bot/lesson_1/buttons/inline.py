from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    print(f"{message.from_user.first_name} : {message.from_user.id}")
    text = f"Hi {message.from_user.first_name}!Welcome to Botirjon Bot"
    await message.answer(text)


@dp.message_handler(commands='inline_button')
async def start_handler(message: types.Message):

    design = [
        [InlineKeyboardButton("Kun Uz" , url="https://kun.uz/") , InlineKeyboardButton("My account" , url="https://t.me/Dilshod_Absaitov")],
        [InlineKeyboardButton("Kun Uz tg" , web_app=WebAppInfo(url= "https://kun.uz/"))]
    ]

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer("Inline keyboard show !", reply_markup=ikm)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
