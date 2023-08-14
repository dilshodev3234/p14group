
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

def change_btn2():

    btn1 = InlineKeyboardButton("Hi_change", callback_data="hi")
    btn2 = InlineKeyboardButton("Hello_change", callback_data="hello")
    markup = InlineKeyboardMarkup()
    markup.add(btn1, btn2)
    return markup

def change_btn1():
    btn1 = InlineKeyboardButton("Hi_change", callback_data="hi")
    markup = InlineKeyboardMarkup()
    markup.add(btn1)
    return markup

@dp.message_handler(commands="start")
async def register_handler(message:types.Message, state : FSMContext):

    await message.answer("Hi", reply_markup=change_btn2())


@dp.callback_query_handler(lambda call: call.data in ("hi" , "hello"))
async def callback_handler(callback: types.CallbackQuery):
    print(callback.data)
    if callback.data == "hi":
        await callback.message.edit_reply_markup( reply_markup=change_btn1())
        await callback.message.edit_reply_markup( reply_markup=change_btn1())
    else:
        await callback.message.edit_reply_markup(reply_markup=change_btn1())


if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)


