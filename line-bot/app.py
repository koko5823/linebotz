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
def handle_message(event):
    if event.message.text==u"時間":
        now = time.localtime()
        print(now)
        t = time.strftime("%H %M", now)
        t = t.split(' ')
        hour = int(t[0]) +8
        minute = int(t[1])
        str(hour)
        str(minute)
        print(hour , minute)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(str(hour)+str(minute)))


    if event.message.text==u"開燈":
        data = {
 "datapoints":[
      {
         "dataChnId":"SWITCH",
         "values":{
            "value":"1"
         }
      }
   ]
}
        ra = requests.post(mcsp, json=data, headers=headers)
        ra.encoding = 'utf-8'
        print(ra.status_code)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(u"不會開"))




    if event.message.text==u"關燈":
        data = {
 "datapoints":[
      {
         "dataChnId":"SWITCH",
         "values":{
            "value":"0"
         }
      }
   ]
}

        rb = requests.post(mcsp, json=data, headers=headers)
        rb.encoding = 'utf-8'
        print(rb.status_code)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(u"關不起來"))


    if event.message.text==u"PH值": #RC讀取JSON的數據，
        rc = requests.get(mcsg, headers=headers)
        rc.encoding = 'utf-8'
        print(rc.status_code)
        doc=json.loads(rc.text)
        print(doc)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(u"幹你娘"))

    if event.message.text =="設定吃藥時間":
        image_url_1 = "https://i.imgur.com/hbthI4f.jpg"
        image_url_2 = "https://i.imgur.com/hbthI4f.jpg"
        click_link_1 = "https://www.facebook.com/ntustcc"
        click_link_2 = "https://www.facebook.com/ntustcc"
        carousel_template = template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=image_url_1,
                    title='早上吃藥時間',
                    text='早上',
                    actions=[
                        MessageTemplateAction(
                            label='早上7點',
                            text='已幫您預約7點'
                            int n = 1
                        ),
                        MessageTemplateAction(
                            label='早上8點',
                            text='已幫您預約8點'
                        ),
                        MessageTemplateAction(
                            label='早上9點',
                            text='已幫您預約9點'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=image_url_1,
                    title='中午吃藥時間',
                    text='中午',
                    actions=[
                        MessageTemplateAction(
                            label='上午11點',
                            text='已幫您預約11點'
                        ),
                        MessageTemplateAction(
                            label='中午12點',
                            text='已幫您預約12點'
                        ),
                        MessageTemplateAction(
                            label='下午1點',
                            text='已幫您預約下午1點'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=image_url_2,
                    title='晚上吃藥時間',
                    text='晚上',
                    actions=[
                        MessageTemplateAction(
                            label='下午5點',
                            text='已幫您預約下午5點'
                        ),
                        MessageTemplateAction(
                            label='下午6點',
                            text='已幫您預約下午6點'
                        ),
                        MessageTemplateAction(
                            label='下午7點',
                            text='已幫您預約下午7點'

                        )
                    ]
                )]
            )
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(alt_text="Carousel Template Example", template=carousel_template))

        if n==1
            print(good)









    else:
       line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
