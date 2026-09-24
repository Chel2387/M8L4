import telebot
import psutil
import TOKEN from config

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, '''Привет! Я твой телеграмм бот''')

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, '''Этот бот сделан для отслеживания состояние системы. 
                             Здесь есть команды: start/help, info, CPU, RAM, UpTime''')

@bot.message_handler(commands=['CPU'])
def CPU(message):
    cpy_count = psutil.cpu_count(logical=False)
    bot.reply_to(message, f"CPU: {cpy_count}")

@bot.message_handler(commands=['RAM'])
def RAM(message):
    ram=psutil.virtual_memory()
    bot.reply_to(message, f"Всего RAM: {ram.total / (1024 ** 3):.2f} GB")

@bot.message_handler(commands=['UpTime'])
def NET(message):
    soooo = psutil.boot_time()
    bot.reply_to(message, f'Cистема была загружена: {time.time() - soooo}')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=telebot.util.update_types)