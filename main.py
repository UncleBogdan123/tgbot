import telebot
from config import token
from botlogic import gen_pass
from botlogic import coin
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['generate_password'])
def send_password(message):
    bot.send_message(message.chat.id, gen_pass(10))

@bot.message_handler(commands=['Coin_Flip'])
def send_result_coin(message):
    bot.send_message(message.chat.id, coin('flip'))

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "English Article Test")
    answer_options = ["a", "an", "the", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We are going to '' park.",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )


@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()