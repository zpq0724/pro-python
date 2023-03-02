from datetime import datetime
# playsound 库可以播放 mp3 格式音乐;
from playsound import  playsound

alarm_time = input('请输入闹钟时间， 示例：09:50:00 am\n')

# 时
alarm_hour = alarm_time[0:2]
alarm_minut = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]

# 上午或者下午
alarm_period = alarm_time[9:11]

print("完成闹装设置...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    #时间判断
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minut == current_minute:
                if alarm_seconds == current_seconds:
                    print('闹钟要响了')
                    # playsound('"D:\software\海鸣威,吴琼 - 老人与海.mp3"')
                    break
