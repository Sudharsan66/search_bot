# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
from requests import *

randomImageText = "Random Image"

randomPImageUrl = "https://picsum.photos/1200"

likes = 0
dislikes = 0

def random_img(update: Update, context: CallbackContext):

    if randomImageText in update.message.text:
        image = get(randomPImageUrl).content
    else:
        image = None
        response = get('http://quotes.stormconsultancy.co.uk/random.json')
        data = response.json()
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Since there are no available images. Here is a Programming quote for you ...!\n\n\n' {data['quote']}'")

    if image:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, caption="")])

        buttons = [[InlineKeyboardButton("👍", callback_data="like")],
                   [InlineKeyboardButton("👎", callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text="Did you like the image?")


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

    global likes, dislikes

    if "like" in query:
        likes += 1

    if "dislike" in query:
        dislikes += 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"{update.message.from_user.username} :: {likes} => likes")
    print(f"likes => {likes} and dislikes => {dislikes}")
