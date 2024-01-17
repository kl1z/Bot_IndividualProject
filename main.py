import os

import telebot
import json

import messages
from config.config import Config
from functions import *


def main():
    bot = telebot.TeleBot(Config.get_data(arg="TG_BOT_API_KEY"))

    def sticker_message(message, *, choice):
        """
        Функция отправки стикера пользователю

        :param message: объект типа Message
        :param choice: вид стикера
        :return: ничего
        :rtype: None
        """
        stickers: dict
        with open('data/stickers/stickers.json', 'r') as file:
            stickers = json.load(file)
        with open(stickers[choice], 'rb') as file:
            bot.send_sticker(message.chat.id, file)

    @bot.message_handler(commands=['start'])
    def start(message):
        try:
            user = message.from_user
            name = user.first_name
            if user.last_name is not None:
                name += ' ' + user.last_name
            bot.send_message(message.chat.id, messages.WELCOME_MESSAGE.format(user.id, name), parse_mode="html")
            sticker_message(message, choice="Salutional")
        except Exception as error:
            bot.send_message(message.chat.id, messages.bot_messages['simple_error'])
            sticker_message(message, choice="Sad")

    @bot.message_handler(commands=['photo_classification'])
    def photo_classification_first_step(message):
        """
        Обработчик команды /photo_classification (1 часть)
        Отправляет сообщение с просьбой прислать фотографию, для дальнейшей обработки

        :param message: объект типа Message
        """
        try:
            bot.send_message(message.chat.id, messages.PHOTO_FOR_MODEL_MESSAGE, parse_mode='html')
            bot.register_next_step_handler(message, photo_classification_second_step)
        except Exception as error:
            bot.send_message(message.chat.id, messages.bot_messages["simple_error"])
            sticker_message(message, choice="Sad")

    def photo_classification_second_step(message):
        """
        Обработчик команды /photo_classification (2 часть)
        Сохраняет изображение, вызывает функцию image_net_classification()
        для классификации изображения с помощью искусственного интелекта
        и отправляет сообщение с результатом работы модели

        :param message: объект типа Message
        """
        try:
            if message.photo is None:
                bot.send_message(message.chat.id, messages.bot_messages['photo_error'], parse_mode='html')
                sticker_message(message, choice="Sad")
            else:
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                with open('temp/classification.png', 'wb') as new_file:
                    new_file.write(downloaded_file)
                answer = image_net_classification()
                if answer != '':
                    bot.reply_to(message, messages.MODEL_MESSAGE.format(answer), parse_mode='html')
                    os.remove('temp/classification.png')
                else:
                    bot.send_message(message.chat.id, messages.bot_messages["photo_classification_error"])
                    sticker_message(message, choice="Sad")
        except Exception as error:
            raise error
            bot.send_message(message.chat.id, messages.bot_messages["simple_error"])
            sticker_message(message, choice="Sad")

    @bot.message_handler(commands=['developer_info'])
    def photo_classification_first_step(message):
        try:
            with open('data/qr/qr_code.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=messages.ABOUT_MESSAGE, parse_mode='html')
            sticker_message(message, choice="Prog")
        except Exception as error:
            bot.send_message(message.chat.id, messages.bot_messages["simple_error"])
            sticker_message(message, choice="Sad")

    @bot.message_handler()
    def not_sorted(message):

        bot.reply_to(message, messages.bot_messages["unknown_command"])
        sticker_message(message, choice="Unknown")

    bot.infinity_polling()


if __name__ == '__main__':
    Config.load_config()
    main()
