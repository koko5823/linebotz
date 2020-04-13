# coding=utf-8
import requests
import json
import time
from flask import Flask, request, abort
from bs4 import BeautifulSoup

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
mcsp = 'https://api.mediatek.com/mcs/v2/devices/DCo0m0wu/datapoints'
mcsg = 'https://api.mediatek.com/mcs/v2/devices/DCo0m0wu/datachannels/SWITCH/datapoints'
headers = {'deviceKey': 'hcAOPdyHqQdlVzO4','Content-Type': 'application/json'}


app = Flask(__name__)
line_bot_api = LineBotApi('DxnTbk1ujZOlYtKgIcVAzvjWLiGp1PHTXdfjj/vnS8guKTW01u0tN0OI71luzlKfwcHPAIX4lBKILQwkr2OSZiJUT7JReyNujUZNPIuk9XPG/xbAnZEH3y6YiDFlX0+/355w/4dI1i6fOJZSWsM/BAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5a14ae8aaf24460f87aa7bb5597727ed')

#下面LINE端RE
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

    if text=='hi':
        line_bot_api.reply_message(
        event.reply_token, 
            TextSendMessage(text="goood"))
                    
                
            
        










    else:
       line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
