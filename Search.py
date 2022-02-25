# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
from requests import *


def search(update: Update, context: CallbackContext):
    """The Search function works by getting the input from the context.args and fetches the result as json from the duckduckgo API"""
    try:
        user_input = ' '.join(context.args[0:])
        user_input = user_input.replace(' ', '+')
        response = get(f'https://api.duckduckgo.com/?q={user_input}&format=json')
        data = response.json()
        # print(data)
        if data:
            topics = data['RelatedTopics']
            try:
                for result in topics:
                    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{result['Result']}\n\n",
                                             parse_mode=ParseMode.HTML)
            except KeyError as e:
                print(e)


        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="No Results Found!!!!")

    except TelegramError as e:
        if str(e) != "Message is not modified": print(e)