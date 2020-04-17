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
    MessageEvent, TextMessage, LocationMessage, TextSendMessage,
    PostbackEvent, DatetimePickerTemplateAction,TemplateSendMessage,
    CarouselTemplate, CarouselColumn, ButtonsTemplate, PostbackTemplateAction,
    MessageTemplateAction, URITemplateAction, LocationSendMessage
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

def clock_check(time):
    now = time.localtime()
    print(now)
    t = time.strftime("%H %M", now)
    t = t.split(' ')
    hour = int(t[0]) +8
    minute = int(t[1])
    local = str(hour)+str(minute)
    settime = int(local)-int(time) #距離預約時間
    return settime

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(str(hour)+":"+str(minute)))


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
        carousel_template =CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=image_url_1,
                    title='早上吃藥時間',
                    text='早上',
                    actions=[
                        DatetimePickerTemplateAction(
                            label='早上',
                            mode='time',
                            data='morning'
                        ),
                        DatetimePickerTemplateAction(
                            label='中午',
                            mode='time',
                            data='noon'
                        ),
                            DatetimePickerTemplateAction(
                            label='晚上',
                            mode='time',
                            data='night'
                        )
                    ]
                ),
                ]
            )
        #data = clock_check(int(event.postback.data))
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(alt_text="Carousel Template Example", template=carousel_template))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage("距離預約時間還有",str(data)))



    else:
       line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'morning':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="已幫您預約"+event.postback.params['time']))
        set = event.postback.params['time']

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title='你的位置', address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )

if __name__ == "__main__":
    app.run()
