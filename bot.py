import telebot
from api import get_weather

token = '7114441838:AAFYazLOheDvCRRUIpz7i2AxQD_yohZsRX0'
bot = telebot.TeleBot(token)
USERS = {}

@bot.message_handler(commands=['start'])
def start(message):
    hello = 'Добрый день! Я бот, показывающий прогноз погоды.'
    bot.send_message(message.chat.id, text=hello)
    change_city(message)

def change_city(message):
    bot.send_message(message.chat.id, text='Укажите название города')
    bot.register_next_step_handler(message, save_city)

def save_city(message):
    USERS[str(message.chat.id)] = message.text
    bot.send_message(message.chat.id, text=f'Город {message.text} успешно сохранен!', reply_markup=menu())

def menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Текущая погода')
    button2 = telebot.types.KeyboardButton('Подробный прогноз на дату')
    button3 = telebot.types.KeyboardButton('Сменить город')
    keyboard.add(button1, button2, button3)
    return keyboard


def current_weather(message):
    try:
        weather = get_weather(USERS[str(message.chat.id)])
        answer = '\n'.join(weather)
    except:
        answer = 'Погода по данному городу не найдена'
    bot.send_message(message.chat.id, text=answer)

@bot.message_handler(content_types=['text'])
def check_text (message):
    if message.text == 'Текущая погода':
        current_weather(message)
    elif message.text == 'Сменить город':
        change_city(message)
    elif message.text == 'Подробный прогноз на дату':
        bot.reply_to(message, 'Данная функция находится в разработке')
    else:
        bot.reply_to(message, 'К сожалению я вас не понимаю') 

bot.polling()