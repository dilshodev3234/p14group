
from aiogram import Bot , Dispatcher , types , executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup



BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(message: types.Message):
    print(message)

@dp.message_handler(commands="photo")
async def photo_handler(message: types.Message):
    await message.answer_photo("https://telegra.ph/file/41975579834f5d70c6469.png")


if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)


