# linebotz
API https://github.com/line/line-bot-sdk-python/blob/master/examples/flask-kitchensink/app.py
---------------------------------------------------------------------------------------------------------------------------------------
# 2020/4/11 Note
I found a linebot api about datetimepicker it mean the templete i make before is bullshit = =

**datetimepicker** can let user type in date / time / datetime data  to  developer follow up .

old code --->

reservation time funcion

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
 
 collect user statue
 
    if event.message.text =="設定吃藥時間":
    carousel_template = template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=image_url_1,
                    title='早上吃藥時間',
                    text='早上',
                    actions=[
                        PostbackAction(
                            label='早上7點',
                            display_text='已幫您預約7點',
                            data='0700'
                        ),
                        PostbackAction(
                            label='早上8點',
                            display_text='已幫您預約8點',
                            data='0800'
                        ),
                        PostbackAction(
                            label='早上9點',
                            display_text='已幫您預約9點',
                            data='0900'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=image_url_1,
                    title='中午吃藥時間',
                    text='中午',
                    actions=[
                        PostbackAction(
                            label='上午11點',
                            display_text='已幫您預約11點',
                            data='1100'
                        ),
                        PostbackAction(
                            label='中午12點',
                            display_text='已幫您預約12點',
                            data='1200'
                        ),
                        PostbackAction(
                            label='下午1點',
                            display_text='已幫您預約下午1點',
                            data='1300'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=image_url_2,
                    title='晚上吃藥時間',
                    text='晚上',
                    actions=[
                        PostbackAction(
                            label='下午5點',
                            display_text='已幫您預約下午5點',
                            data='1700'
                        ),
                        PostbackAction(
                            label='下午6點',
                            display_text='已幫您預約下午6點',
                            data='1800'
                        ),
                        PostbackAction(
                            label='下午7點',
                            display_text='已幫您預約下午7點',
                            data='1900'
                        )
                    ]
                )]
            )
webhook
 
    data = clock_check(event.postback.data)
    line_bot_api.reply_message(event.reply_token,TemplateSendMessage(alt_text="Carousel Template Example",           template=carousel_template))
    line_bot_api.reply_message(event.reply_token,TextSendMessage("距離預約時間還有",str(data)))

##最新科技
   
currently issue
    
