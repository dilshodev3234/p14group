# aiogram ✅
# teleBot
# 1)
# pip install aiogram
from aiogram import Bot , Dispatcher , types , executor

BOT_TOKEN = "6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    print(f"{message.from_user.first_name} : {message.from_user.id}")
    text = f"Hi {message.from_user.first_name}!Welcome to Botirjon Bot"
    await message.answer(text)

@dp.message_handler(commands="info")
async def echo_handler(message: types.Message):
    bot_info = await bot.get_me()
    await message.answer(str(bot_info))


@dp.message_handler(commands="answer")
async def echo_handler(message: types.Message):

    await message.answer("This is answer method !")


@dp.message_handler(commands="reply")
async def echo_handler(message: types.Message):

    await message.reply("This is reply method !")


@dp.message_handler(commands="send_message")
async def echo_handler(message: types.Message):
    await message.bot.send_message(1806940376 , message.text )

@dp.message_handler(commands="send_photo")
async def echo_handler(message: types.Message):
    await message.bot.send_photo(message.chat.id ,"https://telegra.ph/file/b8960d1201093474121b7.png", caption="Python" )

@dp.message_handler(commands="send_video")
async def echo_handler(message: types.Message):
    await message.bot.send_video(message.chat.id ,"https://t.me/Prikollar_qiziqarli_kulguli/23347" )

@dp.message_handler(commands="send_phone")
async def echo_handler(message: types.Message):
    await message.bot.send_contact(message.chat.id ,"998993583235" , "Botirjon", "Qodirov")


@dp.message_handler(commands="send_location")
async def echo_handler(message: types.Message):
    await message.bot.send_location(message.chat.id ,34.345 , 45.98)




@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.bot.send_message( message.from_user.id, f"{message.from_user.first_name}:{message.text}" )





if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)


