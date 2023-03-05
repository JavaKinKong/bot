from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


TOKEN = '6199596406:AAGEq72yQlr2f8AzwAx3SMkm9DmjTvHsYAw'

bot = Bot(TOKEN)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True) #!
b0 = '/алгебра'
b1 = '/геометрия'
b2 = '/физика'
b3 = '/русский язык'

kb.add(b0,b1,b2,b3)

@dp.message_handler(commands=['start'])
async def number_algebra(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text='это бот гдз, выбери паредмет', reply_markup=kb)

@dp.message_handler(commands=['алгебра'])
async def number_algebra(message: types.Message):
    await message.answer('бу')
    await bot.send_photo(chat_id=message.from_user.id,
        photo=('https://reshebnik.school/GDZ/9-rus-rf/1/%27'+message.text.upper()+'%27.png%27'))


if __name__ == '__main__':
    executor.start_polling(dp)
