# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
from requests import *

randomPImageUrl = "https://picsum.photos/1200"


def random_img(update: Update, context: CallbackContext):
    """This Function returns an Random image from PicSum.Photos API"""
    if update.message.text:
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
