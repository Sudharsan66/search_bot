# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
from requests import *

likes = 0
dislikes = 0


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

    global likes, dislikes

    if "like" in query:
        likes += 1

    if "dislike" in query:
        dislikes += 1
    try:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"{likes}:👍\t {dislikes} : 👎",
                                 parse_mode=ParseMode.HTML)
    except AttributeError as e:
        print(e)
    print(f"likes => {likes} and dislikes => {dislikes}")