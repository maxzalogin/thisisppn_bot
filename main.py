import config
import text 
import link

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text.channel, url=link.channel))
    await message.answer(text.start, parse_mode='html', reply_markup=markup)

@dp.message_handler(commands=['support'])
async def support(message: types.Message):
    await message.answer(text.support)

@dp.message_handler(commands=['conf'])
async def conf(message: types.Message):
     markup = types.InlineKeyboardMarkup()
     btn_iphone = types.InlineKeyboardButton('🍏 - iPhone', callback_data='iphone')
     btn_android = types.InlineKeyboardButton('🤖 - Android', callback_data='android')
     markup.row(btn_iphone, btn_android)
     # btn_windows =types.InlineKeyboardButton('🔍 - Windows', callback_data='windows')
     # markup.row(btn_windows)
     await message.reply(text.install, reply_markup=markup)

@dp.message_handler(commands=['pay'])
async def payment(message: types.Message):
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton('Оплатить доступ', url=link.donate))
     await message.reply(text.subscribe, reply_markup=markup, parse_mode='html')

@dp.callback_query_handler()
async def callback(callback_query: types.CallbackQuery):
        if callback_query.data == 'android':
            # file = open('android.jpg', 'rb')
            await callback_query.message.answer(text.android)
        if callback_query.data == 'windows':
            await callback_query.message.answer(text.windows)
        elif callback_query.data == 'iphone':
            # file = open('android.jpg', 'rb')
            await callback_query.message.answer(text.iphone)
            
@dp.message_handler()
async def other(message: types.Message):
      await message.answer(text.not_commands)

executor.start_polling(dp, skip_updates=True)