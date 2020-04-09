#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import configparser
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from fugle_realtime import intraday

#(03/27更新）試試看
from telegram import ReplyKeyboardMarkup


# In[2]:


config = configparser.ConfigParser()
config.read('config.ini')


# In[3]:


config['TELEGRAM']['ACCESS_TOKEN']


# In[4]:


config['TELEGRAM']['WEBHOOK_URL']


# In[5]:


access_token = config['TELEGRAM']['ACCESS_TOKEN']
webhook_url = config['TELEGRAM']['WEBHOOK_URL']


# In[8]:


print(webhook_url)


# ## delete webhook url

# In[95]:


requests.post('https://api.telegram.org/bot'+access_token+'/deleteWebhook').text


# ## set webhook url

# In[6]:


print('https://api.telegram.org/bot'+access_token+'/setWebhook?url='+webhook_url+'/hook')


# In[7]:


requests.post('https://api.telegram.org/bot'+access_token+'/setWebhook?url='+webhook_url+'/hook').text


# In[12]:


# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=config['TELEGRAM']['ACCESS_TOKEN'])





#(0327更新)

reply_keyboard_markup = ReplyKeyboardMarkup([['開盤價'],
                                             ['最高價'],
                                             ['最低價'],
                                             ['收盤價'],
                                             ['交易量總和']])

wel = "請輸入股票代碼"

api_token = 'ded8e2378294127b01e4003ce15ff067'


@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        #固定的東西不用管
        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'


def start_handler(bot, update):
    update.message.reply_text(wel)
    
    
    
    
## reply message
def reply_handler(bot, update):
    text = update.message.text
    user_id = update.message.from_user.name
    
    if text in symbolId_dic['symbolId']:
        K_data = intraday.chart(apiToken=api_token,symbolId=str(text))
        #開盤價
        a = str(K_data.tail(1)['open'])
        b = a.split(sep='    ')[1]
        o = b.split(sep='N')[0]
        
        a = str(K_data.tail(1)['close'])
        b = a.split(sep='    ')[1]
        close = b.split(sep='N')[0]
        
        a = str(K_data.tail(1)['high'])
        b = a.split(sep='    ')[1]
        high = b.split(sep='N')[0]
        
        a = str(K_data.tail(1)['low'])
        b = a.split(sep='    ')[1]
        low = b.split(sep='N')[0]
        
        a = str(K_data.tail(1)['unit'])
        b = a.split(sep='    ')[1]
        unit = b.split(sep='N')[0]
        
        

        tt = '開盤價：'+o +                   '收盤價：'+ close +                    '最高價：'+ high +                    '最低價：'+low+                    '交易量：'+unit 
        update.message.reply_text(tt)
    else:
        t = '請換一個輸入'
        update.message.reply_text(t)
#         t = '你想知道的是？'
#         text_1=text
#         update.message.reply_text(t,reply_markup=reply_keyboard_markup)
        

#     elif text == '開盤價':
#         #opening='時間：'+K_data.tail(1)['at']+'開盤價為：'+K_data.tail(1)['open']
#         update.message.reply_text(K_data.tail(1)['open'])
#     else:
#         if text == '開盤價':
#             K_data = intraday.chart(apiToken=api_token,symbolId=str(text_1))
#             opening = K_data.tail(1)['open']
#             update.message.reply_text(opening)
#         else:  
#             update.message.reply_text('換一個試試！')
        #update.message.reply_text(text)
    



    
# This class dispatches all kinds of updates to its registered handlers.
dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))


if __name__ == '__main__':
    app.run()


# In[8]:


import pandas as pd


# In[9]:


stock = pd.read_excel('/Users/Rebeca/0319_ntu_scu/fugle_telegram_chatbot/symbol_info.xlsx')


# In[10]:


symbolId=[]
for s in stock['symbol_id']:
    symbolId.append(s)


# In[11]:


symbolId_dic = {'symbolId':symbolId}
print(symbolId_dic)


# In[ ]:




