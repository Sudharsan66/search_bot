# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
import pyttsx3
from gtts import gTTS


def getVoice(update: Update, context: CallbackContext):
    user_input = ' '.join(context.args[0:])
    if user_input:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Hello!!!",
                                 parse_mode=ParseMode.HTML)
        answer = f" The audio requested by {update.message.from_user.username}"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'{answer}',
                                 parse_mode=ParseMode.HTML)
        generateVoice(user_input)
        context.bot.send_audio(chat_id=update.effective_chat.id,
                               audio=open("saved_audio.mp3", "rb"))
    else:
        answer = f"Hello {update.message.from_user.username} I am a chat bot coded with python."
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"{answer}",
                                 parse_mode=ParseMode.HTML)


def generateVoice(user_input):
    engine = pyttsx3.init()
    tts = gTTS(text=user_input, lang='en', slow=False)
    tts.save("saved_audio.mp3")
    print("File saved!")
    engine.setProperty('rate', 200)
    # engine.say("I will speak this text")
    engine.say(user_input)
    engine.runAndWait()
    return engine
