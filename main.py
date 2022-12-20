import telebot

bot = telebot.TeleBot('5978680546:AAHypckClHzS677zrQDn9jGngTLf_lmPxgQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Salom, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Assalomu Aleykum !':
       bot.send_message(message.chat.id, "Sizga ham Salom !", parse_mode='html')
    elif message.text == 'photo':
        photo = open('Warcraft3TFT_1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Sizni chuna olmayaman !', parse_mode ='html')