import telebot
import random

bot = telebot.TeleBot('')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши привет")


# Заготовка

first = [1, 2, 3, 4, 5]

second = [1, 2, 3, 4, 5]

second_add = [1, 2, 3, 4, 5]

third = [1, 2, 3, 4, 5]

print("1 — 1")

print("2 — 2")

wer = int(input("{blue}Введите число: {endcolor}".format(blue="\033[96m", endcolor="\033[0m")))

if 0 < wer < 13:

    print(random.choice(first), random.choice(second), random.choice(second_add), random.choice(third))

else:

    print("Вы ошиблись с числом, запустите программу ещё раз")

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
