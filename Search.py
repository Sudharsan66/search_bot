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
        if data:
            topics = data['RelatedTopics']
            for result in topics:
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{result['Result']}</b>\n\n<a href='{result['FirstURL']}'> </a>",
                                         parse_mode=ParseMode.HTML)

        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="No Results Found!!!!")

    except TelegramError as e:
        if str(e) != "Message is not modified": print(e)