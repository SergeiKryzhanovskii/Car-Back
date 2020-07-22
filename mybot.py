import telebot
import wikipedia
import config
from telebot import types

"""Функция поиска в Вики"""
def search_wiki(query):
    global language
    wikipedia.set_lang(language)
    result = wikipedia.summary(query)
    return result


"""Функция вывода ссылки на статью"""
def return_url(query):
    global language
    wikipedia.set_lang(language)
    result = wikipedia.page(query)
    url = result.url
    return url


"""Эмоджи"""
glass = u'\U0001F50E'

bot = telebot.TeleBot(config.token)
language = 'ru'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    photo = open('photo_bot.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)
    msg = 'Привет, я бот-помощник для поиска в Википедии.\n' + 'Напиши мне, что нужно найти ' + glass + ':'
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtna = types.KeyboardButton('В начало')
    itembtnv = types.KeyboardButton('Мне повезёт!')
    itembtnc = types.KeyboardButton('Настройка')
    markup.add(itembtna, itembtnv, itembtnc)
    bot.send_message(message.from_user.id, msg, reply_markup=markup)


@bot.message_handler(commands=['random'])
def random_page(message):
    random_pg = wikipedia.random(pages=1)
    red = search_wiki(random_pg)
    bot.send_message(message.from_user.id, red)
    url = return_url(random_pg)
    bot.send_message(message.from_user.id, url)


@bot.message_handler(commands=['language'])
def change_language(message):
    pass


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    query = message.text
    msg = search_wiki(query)
    bot.send_message(message.from_user.id, msg)
    url = return_url(query)
    bot.send_message(message.from_user.id, url)


bot.polling(none_stop=True, interval=0)
