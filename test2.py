import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'go'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет " + message.from_user.first_name + ", я считаю индекс массы тела")
    message = bot.send_message(message.chat.id, "Какой у тебя рост? \nПример 1.5")
    bot.register_next_step_handler(message, get_h)

def get_h(message): #получаем рост
    global h 
    h = float(message.text)
    message = bot.send_message(message.from_user.id, 'Какой у тебя вес? \nПример 45')
    bot.register_next_step_handler(message, get_w)

def get_w(message): #получаем вес
    global w 
    w = int(message.text)
    result = calc(h, w)
    bot.send_message(message.chat.id, result)

def calc(h, w):
        BMI = w / (h ** 2)

        if BMI < 18.5:
            result = f"Твой ИМТ = {BMI}.\nЕшь побольшe"
        elif BMI >= 18.5 and BMI <= 24.9:
            result = f"Твой ИМТ = {BMI}.\nВсё чётенько"
        elif BMI >= 25.0 and BMI <= 29.9:
            result = f"Твой ИМТ = {BMI}.\nНемного лишка"
        else:
            result = f"Твой ИМТ = {BMI}.\nЧто-то ты переборщил с едой, пора на треню"
        
        return result

bot.delete_webhook()

if __name__ == '__main__':
     bot.polling(none_stop=True, interval = 0)
