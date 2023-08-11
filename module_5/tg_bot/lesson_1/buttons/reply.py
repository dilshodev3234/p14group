from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    print(f"{message.from_user.first_name} : {message.from_user.id}")
    text = f"Hi {message.from_user.first_name}!Welcome to Botirjon Bot"
    await message.answer(text)

@dp.message_handler(commands='reply_button')
async def start_handler(message: types.Message):

    # markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add("Button 1" ,"Button 2")
    # markup.add("Button 3")
    # markup.add("Button 3")
    # markup.add("Button 4")

    design = [
        ["/start", "/Button 2", KeyboardButton("☎️Phone number", request_contact=True), "Button 4"],
        ["Button 5", "Button 6", KeyboardButton("📍 Location", request_location=True), "Button 8"]
    ]
    markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


    await message.answer("Reply button show" , reply_markup=markup)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
