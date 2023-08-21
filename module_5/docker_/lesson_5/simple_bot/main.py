import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cats(message: types.Message):
    await message.answer("Welcome to bot !")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)