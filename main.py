import os
import telebot
from config.config import Config
import messages
def main():
    bot = telebot.TeleBot(Config.get_data(arg="TG_BOT_API_KEY"))

    @bot.message_handler()
    def not_sorted(message):
        bot.reply_to(message, messages.bot_messages["unknown_command"])

    bot.infinity_polling()


if __name__ == '__main__':
    main()