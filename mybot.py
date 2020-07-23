import telebot
import wikipedia
import config
from telebot import types
from wikipedia import exceptions


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
    itembtn_start = types.KeyboardButton('В начало')
    itembtn_random = types.KeyboardButton('Мне повезёт!')
    itembtn_settings = types.KeyboardButton('Настройка')
    markup.add(itembtn_start, itembtn_random, itembtn_settings)
    bot.send_message(message.from_user.id, msg, reply_markup=markup)


@bot.message_handler(commands=['random'])
def random_page(message):
    try:
        random_pg = wikipedia.random(pages=1)
        red = search_wiki(random_pg)
        bot.send_message(message.from_user.id, red)
        url = return_url(random_pg)
        bot.send_message(message.from_user.id, url)
    except wikipedia.exceptions.DisambiguationError:
        msg = 'Упс, я озадачен твоим запросом, уж больно много вариантов. \nПопробуй уточнить:'
        bot.send_message(message.from_user.id, msg)
    except wikipedia.exceptions.HTTPTimeoutError:
        msg = 'Упс, видимо, мне не хотят отвечать... \nДавай  подождём, пусть они там немного разгрузятся.'
        bot.send_message(message.from_user.id, msg)
    except wikipedia.exceptions.PageError:
        msg = 'Упс, видимо, такой статьи не существует... \nПопробуй поискать что-нибудь другое.'
        bot.send_message(message.from_user.id, msg)
    except wikipedia.exceptions.RedirectError:
        msg = 'Упс, нас пытаютсякуда-то перенаправить... \nПопробуй поискать еще раз.'
        bot.send_message(message.from_user.id, msg)
    except wikipedia.exceptions.WikipediaException:
        msg = 'Упс, что-то пошло не так... \nПопробуй поискать еще раз.'
        bot.send_message(message.from_user.id, msg)


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    if message.text == 'В начало':
        send_welcome(message)
    elif message.text == 'Мне повезёт!':
        random_page(message)
    elif message.text == 'Настройка':
        keyboard = types.InlineKeyboardMarkup()
        key_ru = types.InlineKeyboardButton(text='ru', callback_data='val_ru')
        keyboard.add(key_ru)
        key_en = types.InlineKeyboardButton(text='en', callback_data='val_en')
        keyboard.add(key_en)
        bot.send_message(message.from_user.id, text='Выбери язык, на котором тебе нужно напечатать статью.', reply_markup=keyboard)
    else:
        try:
            query = message.text
            msg = search_wiki(query)
            bot.send_message(message.from_user.id, msg)
            url = return_url(query)
            bot.send_message(message.from_user.id, url)
        except wikipedia.exceptions.DisambiguationError:
            msg = 'Упс, я озадачен твоим запросом, уж больно много вариантов. \nПопробуй уточнить:'
            bot.send_message(message.from_user.id, msg)
        except wikipedia.exceptions.HTTPTimeoutError:
            msg = 'Упс, видимо, мне не хотят отвечать... \nДавай  подождём, пусть они там немного разгрузятся.'
            bot.send_message(message.from_user.id, msg)
        except wikipedia.exceptions.PageError:
            msg = 'Упс, видимо, такой статьи не существует... \nПопробуй поискать что-нибудь другое.'
            bot.send_message(message.from_user.id, msg)
        except wikipedia.exceptions.RedirectError:
            msg = 'Упс, нас пытаютсякуда-то перенаправить... \nПопробуй поискать еще раз.'
            bot.send_message(message.from_user.id, msg)
        except wikipedia.exceptions.WikipediaException:
            msg = 'Упс, что-то пошло не так... \nПопробуй поискать еще раз.'
            bot.send_message(message.from_user.id, msg)


@bot.callback_query_handler(func=lambda call: True)
def call_worker(call):
    global language
    if call.data == 'val_ru':
        wikipedia.set_lang('ru')
        language = 'ru'
    elif call.data == 'val_en':
        wikipedia.set_lang('en')
        language = 'en'



bot.polling(none_stop=True, interval=0)
