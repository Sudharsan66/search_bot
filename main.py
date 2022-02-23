# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
from requests import *

import Search
import image
import randomImg

updater = Updater(token="5149900814:AAGFE0NiLbSk0hUmXZ-Os5RJzu6q-xu-9Gs")
dispatcher = updater.dispatcher

randomImageText = "Random Image"

allowedUsernames = ["sudharsan5047"]


def startCommand(update: Update, context: CallbackContext):
    """This is where the bot is initiated - /start command"""
    buttons = [[KeyboardButton(randomImageText)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to your custom Search Engine!",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def check_permission(update: Update, context: CallbackContext):
    """The username is validated is there are permissions for accessing the functions or not"""
    try:
        if update.effective_chat.username not in allowedUsernames:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"{update.message.from_user.username} :: You are not allowed to use this bot")
            return
    except TelegramError as e:
        if str(e) != "Message is not modified": print(e)


dispatcher.add_handler(CommandHandler("start", startCommand))
# dispatcher.add_handler(MessageHandler(Filters.text, check_permission))
dispatcher.add_handler(CommandHandler("random", randomImg.random_img))
dispatcher.add_handler(CallbackQueryHandler(randomImg.queryHandler))
dispatcher.add_handler(CommandHandler('search', Search.search))
dispatcher.add_handler(CommandHandler('img', image.image_search))

updater.start_polling()
