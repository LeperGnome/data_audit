import telebot
import time
from random import choice
from bot_token import token


bot = telebot.TeleBot(token)

responses = [
    '''
    Категория услуги: Клининг\nПлощадь (м²): 562.25\nКол-во дней: 120\nЦена (р): 74892.00\n\nВердикт: Сильных отклонений не выявлено.
    ''',
    '''
    Категория услуги: Охрана\nПлощадь (м²): 244.7\nКол-во дней: 130\nЦена (р): 92842.85\n\nВердикт: Сильных отклонений не выявлено.
    ''',
    '''
    Категория услуги: Клининг\nПлощадь (м²): 312.5\nКол-во дней: 61\nЦена (р): 52119.00\n\nВердикт: Сильных отклонений не выявлено.
    '''
]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я КДЗ.\nКидай мне договор, проверим его на подозрительность!\nЯ пока не очень умный, мои создатели надо мной работают.')


@bot.message_handler(content_types=['document'])
def send_doc(message):
    time.sleep(5)
    bot.send_message(message.chat.id, choice(responses))


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'Я жду документ...')


bot.polling()
