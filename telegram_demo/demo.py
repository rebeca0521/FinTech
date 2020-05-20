#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import configparser
import telegram
from flask import Flask, request
from telegram import ReplyKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
#from fugle_realtime import intraday


# In[2]:


config = configparser.ConfigParser()
config.read('config.ini')


# In[3]:


access_token = config['TELEGRAM']['ACCESS_TOKEN']
webhook_url = config['TELEGRAM']['WEBHOOK_URL']


# In[4]:


requests.post('https://api.telegram.org/bot'+access_token+'/setWebhook?url='+webhook_url+'/hook').text


# In[5]:


# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=config['TELEGRAM']['ACCESS_TOKEN'])





#(0327更新)

reply_keyboard_markup = ReplyKeyboardMarkup([['/Knowledge Graph of the Week'],
                                             ['/相關新聞'],
                                             ['/其他']])

wel = "想知道最近發生什麼事嗎？"



@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        #固定的東西不用管
        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'


def start_handler(bot, update):
    update.message.reply_text(wel, reply_markup=reply_keyboard_markup)
      
    
    
    
def help_handler(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text(welcome_message, reply_markup=reply_keyboard_markup)    
    
    
## reply message
def reply_handler(bot, update):
    """Reply message."""
    text = update.message.text
    update.message.reply_text(text)
    




    
# This class dispatches all kinds of updates to its registered handlers.
dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))


if __name__ == '__main__':
    app.run()


# In[ ]:




