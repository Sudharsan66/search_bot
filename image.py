# -*- coding: utf-8 -*-
import requests
from telegram import *
from telegram.ext import *
import re
import json

likes = 0
dislikes = 0


def image_search(update: Update, context: CallbackContext, max_results=None):
    """The image_search function works by getting the input from the context.args and fetches the result as images from the duckduckgo API"""
    User_input = ' '.join(context.args[0:])
    User_input = User_input.replace(' ', '+')
    # print(User_input)
    url = 'https://duckduckgo.com/'
    params = {
        'q': User_input
    }

    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M | re.I)
    if not searchObj:
        return -1

    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('l', 'us-en'),
        ('o', 'json'),
        ('q', User_input),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '1'),
        ('v7exp', 'a'),
    )

    requestUrl = url + "i.js"

    # while True:
    #     while True:
    try:
        res = requests.get(requestUrl, headers=headers, params=params)
        data = json.loads(res.text)
        # break
    except ValueError as e:
        print(e)
        # continue

    img_data = data["results"]
    for index, obj in enumerate(img_data):
        if index < 5:
            if obj['image']:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f"<a href='{obj['image']}'>.</a>\n\n",
                                         parse_mode=ParseMode.HTML)
                buttons = [[InlineKeyboardButton("👍", callback_data="like")],
                           [InlineKeyboardButton("👎", callback_data="dislike")]]
                context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                         text="Did you like the image?")
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Image Not Found!!!!",
                                         parse_mode=ParseMode.HTML)
        elif index > 5:
            break
    if "next" not in data:
        exit(0)

    requestUrl = url + data["next"]

