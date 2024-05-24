import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("введите ваш токен")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить водичку! И не отвлекаться!')
    reminder_thread = threading.Thread(target=send_reminder, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['focus'])
def focus_message(message):
    bot.reply_to(message, 'Начали! Работа без отвлечений - 25 мин')
    reminder_thread2 = threading.Thread(target=focus_timer, args=(message.chat.id,))
    reminder_thread2.start()


@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ["Вода является единственным веществом на Земле, которое может существовать в трех агрегатных состояниях: жидком, твердом и газообразном.", "Вода имеет высокое удельное теплоемкость, что делает ее отличным теплоносителем и позволяет регулировать температуру окружающей среды.",
"Вода обладает уникальными свойствами поверхностного натяжения, благодаря которым она образует капли и позволяет насекомым ходить по поверхности воды без тонутя."]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде: {random_fact}')

def send_reminder(chat_id):
    first_rem = "09:00"
    second_rem = "14:00"
    end_rem = "18:00"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)

def focus_timer(chat_id):
    time.sleep(1500)
    bot.send_message(chat_id, "Цель достигнута! Вы сосредоточено работали. Теперь можно отдохнуть 5 мин.")
    time.sleep(295)
    for i in range(5):
        bot.send_message(chat_id, 5-i)
        time.sleep(1)

    bot.send_message(chat_id, "Начали! Работа без отвлечений - 25 мин")
    time.sleep(5)
    bot.send_message(chat_id, "Цель достигнута! Можно отдохнуть.")

bot.polling(none_stop=True)