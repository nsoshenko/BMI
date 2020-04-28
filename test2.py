from BMI import config
import telebot

h = ''
w = ''

bot = telebot.TeleBot(config.token)

@bot.message_handler(coommands=['start', 'go'])
def welcome(message):
    message = bot.send_message(message.chat.id, "Привет " + message.from_user.first_name + "я считаю индекс массы тела")
    bot.register_next_step_handler(message, get_h)

def get_h(message): #получаем рост
    global h
    h = float(message.text)
    bot.send_message(message.from_user.id, 'Какой у тебя рост? \nПример 1.5')
    bot.register_next_step_handler(message, get_w)

def get_w(message): #получаем вес
    global w
    w = int(message.text)
    bot.send_message(message.from_user.id, 'Какой у тебя вес? \nПример 45')
    bot.register_next_step_handler(message, calc)

def calc():
        BMI = w / (h ** 2)

        return f'Твой ИМТ = {BMI}'

bot.delete_webhook()

if __name__ == '__main__':
     bot.polling(none_stop=True, interval = 0)
