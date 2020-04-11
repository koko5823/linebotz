# linebotz
---------------------------------------------------------------------------------------------------------------------------------------
# 2020/4/11 Note
I found a linebot api about datetimepicker it mean the templete i make before is bullshit = =
**datetimepicker** can let user type in date / time / datetime data  to  developer follow up .

old code --->

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
