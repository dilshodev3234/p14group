
from aiogram import Bot , Dispatcher , types , executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Register(StatesGroup):
    fullname = State()
    phone_number = State()


@dp.message_handler(commands="register")
async def register_handler(message:types.Message, state : FSMContext):
    await Register.fullname.set()
    await message.answer("To'liq ism familya : ")

@dp.message_handler(state = Register.fullname)
async def fullname_handler(message: types.Message , state: FSMContext):

    async with state.proxy() as data:
        data["fullname"] = message.text
    # await state.set_data({"fullname": message.text})
    await Register.next()
    markup = ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard=True)
    markup.add(KeyboardButton("☎️phone number", request_contact=True))
    await message.answer("Pasdagi tugmani bosib nomerizni yuboring: ", reply_markup=markup)

@dp.message_handler(content_types=types.ContentTypes.CONTACT,state = Register.phone_number)
async def contact_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone"] = message.contact.phone_number
    # data = await state.get_data()
    # data['phone'] = message.text
    # await state.set_data(data)
    data = await state.get_data()
    text = f"""Fullname : {data.get("fullname")}
☎️phone : {data.get("phone")}"""
    await message.answer(text)
    await state.finish()
    await message.answer("Tabriklimiz siz mofaqiyatli royhatdan o'tdingniz !" )











if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)


