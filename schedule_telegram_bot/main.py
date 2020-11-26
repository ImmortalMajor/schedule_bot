import telebot
from credentials import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Fucking Slave')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, 'Fucking Slave')


def main():
    bot.polling()


if __name__ == '__main__':
    main()
