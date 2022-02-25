# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
from requests import *

import Search
import image
import queryHandler
import randomImg
import voice

updater = Updater(token="5067785773:AAHikkvebWKMYrbMmoNNWKiUoRGkUUEzUQ0")
dispatcher = updater.dispatcher

Help = 'Help'


def startCommand(update: Update, context: CallbackContext):
    """This is where the bot is initiated - /start command"""
    buttons = [[KeyboardButton('Help')]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to the DuckDuckGo search engine and text to speech bot",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def help(update: Update, context: CallbackContext):
    if update.message.text == 'Help':
        """The Help function displays all the available methods and the usages of them"""
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="<b>List of commands:</b>\n\n"
                                      "<b>/start</b> - \tStarts the bot...!\n"
                                      "<b>/search</b> - \tTakes an argument and searches the DuckDuckGo Api for that keyword\n "
                                      "<b>/img</b> - \tTakes an argument and search the DuckDuckGo Api for images of that keyword\n"
                                      "<b>/random</b> - \tDisplays a random image obtained from picsum api\n"
                                      "<b>/voice</b> - \ttakes an argument and converts it into audio using python text to speech X3 - pptyx3 - package",
                                 parse_mode=ParseMode.HTML)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="<b>List of commands:</b>\n\n"
                                      "<b>/start</b> - \tStarts the bot...!\n"
                                      "<b>/search</b> - \tTakes an argument and searches the DuckDuckGo Api for that keyword\n "
                                      "<b>/img</b> - \tTakes an argument and search the DuckDuckGo Api for images of that keyword\n"
                                      "<b>/random</b> - \tDisplays a random image obtained from picsum api\n"
                                      "<b>/voice</b> - \ttakes an argument and converts it into audio using python text to speech X3 - pptyx3 - package",
                                 parse_mode=ParseMode.HTML)


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.regex(r"Help"), help))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("random", randomImg.random_img))
dispatcher.add_handler(CallbackQueryHandler(queryHandler.queryHandler))
dispatcher.add_handler(CommandHandler('search', Search.search))
dispatcher.add_handler(CommandHandler('img', image.image_search))
dispatcher.add_handler(CommandHandler('voice', voice.getVoice))

updater.start_polling()
