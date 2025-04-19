from imaplib import Commands
import telebot
from aiogram.types import ContentType,Message
import random



bot = telebot.TeleBot('7845718636:AAEk5BnWkaVwYKIDKDcyee4jDpwq2EpJqLE')


@bot.message_handler(commands=['about_me'])
def handle_boring(message):
    bot.send_message(message.chat.id, "скучно, мне скучно..*звуки эха*..скучно.. /schedule, /about_me")

@bot.message_handler(commands=['boring'])
def handle_nothing(message):
    bot.send_message(message.chat.id, ".-- ... .  - .- -.- --- .  .--. ..- ... - --- . .-.-.-  .-- . --.. -.. .  - . -- -. --- .-.-.-  -. .. ---. . --. ---  -. .  .-- .. -.. -. --- .-.-.-  .-.-.- .-.-.- ... -.- ..- ---. -. --- .-.-.- .-.-.-    -..-. -. .. ---. . --. ---")

@bot.message_handler(commands=['nothing'])
def handle_nothing(message):
    bot.send_message(message.chat.id, "-.- .- -.-  .-.-  --.. -.. . ... -..-  --- -.- .- --.. .- .-.. ... .-.- ..--..  ---. - ---  ..-.. - ---  --.. .-  -- . ... - --- ..--..  .--. --- ---. . -- ..-  ..-.. - ---  -- . ... - ---  - .- -.- --- .  .--. ..- ... - --- . ..--..  -.--. --...  -.- .-.. .- ... ... -.--.-")


@bot.message_handler(commands=['place'])
def handle_nothing(message):
    bot.send_message(message.chat.id, "... -.- --- .-.. -..- -.- ---  .-.-  ..- ...- .  --.. -.. . ... -..-  -. .- .... --- ...- ..- ... -..- ..--..  .-- .-. . -- .-.-  --.. -.. . ... -..-  .-- --- --- -... --.- .  . ... - -..- ..--..  .-.-  -. .- .-- . .-. -. --- .  ..- ...- .  --.. -.. . ... -..-  ..--- ----- -....- .---- .....  -- . ... .-.- -.-. . .--   .. .-.. ..  .-.. . -")



@bot.message_handler(commands=['11class'])
def handle_schedule(message):
    pg11 = ['bot_boring/все фотки расписаний/11/11 класс.jpg','bot_boring/все фотки расписаний/11/68800654.jpg']
    rand = random.choice(pg11)
    bot.send_photo(message.chat.id,open(rand, 'rb'))

@bot.message_handler(commands=['10class'])
def handle_schedule(message):
    pg10 = ['bot_boring/все фотки расписаний/10/10 класс.jpg','bot_boring/все фотки расписаний/10/68800654.jpg']
    rand = random.choice(pg10)
    bot.send_photo(message.chat.id,open(rand, 'rb'))
    
@bot.message_handler(commands=['9class'])
def handle_schedule(message):
    pg9 = ['bot_boring/все фотки расписаний/9/9 класс.jpg','bot_boring/все фотки расписаний/9/68800654.jpg']
    rand = random.choice(pg9)
    bot.send_photo(message.chat.id,open(rand, 'rb'))

@bot.message_handler(commands=['8class'])
def handle_schedule(message):
    pg8 = ['bot_boring/все фотки расписаний/8/8 класс.jpg','bot_boring/все фотки расписаний/8/68800654.jpg']
    rand = random.choice(pg8)
    bot.send_photo(message.chat.id,open(rand, 'rb'))

@bot.message_handler(commands=['7class'])
def handle_schedule(message):
    pg7 = ['bot_boring/все фотки расписаний/7/-pyUkJPBP7I.jpg','bot_boring/все фотки расписаний/7/Расписание-11-классов001.png']
    rand = random.choice(pg7)
    bot.send_photo(message.chat.id,open(rand, 'rb'))

@bot.message_handler(commands=['6class'])
def handle_schedule(message):
    pg6 = ['bot_boring/все фотки расписаний/6/09040486.jpg','bot_boring/все фотки расписаний/6/Raspisanie_urokov_v_10_a_klasse_na-42975.jpg']
    rand = random.choice(pg6)
    bot.send_photo(message.chat.id,open(rand, 'rb'))

@bot.message_handler(commands=['5class'])
def handle_schedule(message):
    pg5 = ['bot_boring/все фотки расписаний/5/5класс.jpg','bot_boring/все фотки расписаний/5/raspisanie_urokov_osnovnaja_shkola_1_smena.jpg']
    rand = random.choice(pg5)
    bot.send_photo(message.chat.id,open(rand, 'rb'))


@bot.message_handler(commands=['schedule'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    class11 = telebot.types.KeyboardButton(text="/11class")
    class10 = telebot.types.KeyboardButton(text="/10class")
    class9 = telebot.types.KeyboardButton(text="/9class")
    class8 = telebot.types.KeyboardButton(text="/8class")
    class7 = telebot.types.KeyboardButton(text="/7class")
    class6 = telebot.types.KeyboardButton(text="/6class")
    class5 = telebot.types.KeyboardButton(text="/5class")
    keyboard.add(class11,class10,class9,class8,class7,class6,class5)
    bot.send_message(chat_id,
                     'в каком классе',
                     reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    scedule = telebot.types.KeyboardButton(text="/schedule")
    about_me = telebot.types.KeyboardButton(text="/about_me")

    keyboard.add(about_me,scedule)
    bot.send_message(chat_id,
                     'добрый день. я ..... я бот для школьников которым не знают какие у них уроки',
                     reply_markup=keyboard)
bot.infinity_polling()
