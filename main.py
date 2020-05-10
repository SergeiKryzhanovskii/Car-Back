import telebot
import random
import urllib.request





bot = telebot.TeleBot('')

urllib.request.urlopen("""
    https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}
""".format(
    API_TOKEN = '',
    CHAT_ID = '0',
    TEXT = 'TEST TEST TEST'
))

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши привет")

bot.polling(none_stop=True, interval=0)




# Заготовка

first = [1, 2, 3, 4, 5]

second = [1, 2, 3, 4, 5]

second_add = [1, 2, 3, 4, 5]

third = [1, 2, 3, 4, 5]


print("1 — 1)

print("2 — 2")



wer = int(input("{blue}Введите число: {endcolor}".format(blue="\033[96m", endcolor="\033[0m")))

if 0 < wer < 13:

    print(random.choice(first), random.choice(second), random.choice(second_add), random.choice(third))

else:

    print("Вы ошиблись с числом, запустите программу ещё раз")



