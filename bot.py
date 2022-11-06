import telebot	# pip install pyTelegramBotAPI
import datetime as dt
import time
import image_handler as image
from telebot import types

bot = telebot.TeleBot('Your token')	# your token from BotFather

def run():
	print('Бот запущен', f'{dt.datetime.now()}')
	bot.polling(none_stop=True)
	
	

# func handling command /start from user chat
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(
		message.chat.id,
		"Привет. Показать одну фотографию, нажми кнопку: 'Фото'\nПоказать серию из 10 фотографий нажми: 'Фото-тайм'",
		reply_markup=foto)


# handling push button 'Фото', send one foto
@bot.callback_query_handler(func=lambda call: call.data == 'foto')
def show_foto(call):
	print('отправил одну рандомную фотку', f'{dt.datetime.now()}, user_id: {call.from_user.id}, username: {call.from_user.username}')
	img = image.get_foto()
	bot.send_photo(call.message.chat.id, img)
	bot.send_message(call.message.chat.id, "Еще фото?", reply_markup=foto)


# handling push button 'Фото_тайм' send ten foto with interval 10 seconds/foto
@bot.callback_query_handler(func=lambda call: call.data == 'foto_time')
def show_foto(call):
	print('запуск foto_time', f'{dt.datetime.now()}, user_id: {call.from_user.id}, username: {call.from_user.username}')
	foto_counter = 10
	while foto_counter:
		img = image.get_foto()
		bot.send_photo(call.message.chat.id, img)
		foto_counter -= 1
		time.sleep(10)
	bot.send_message(call.message.chat.id, "Еще фото?", reply_markup=foto)
	print('завершение foto_time', f'{dt.datetime.now()}, user_id: {call.from_user.id}, username: {call.from_user.username}')
	
# inline buttons
but_foto = types.InlineKeyboardButton(text="Фото", callback_data="foto")
but_foto_time = types.InlineKeyboardButton(text="Фото-Тайм", callback_data="foto_time")

foto = types.InlineKeyboardMarkup(row_width=2)
foto.add(but_foto, but_foto_time)
