#!  /usr/local/bin/python3
#   main.py
#   codeing:UTF-8
import down_timer
#import argument_process

#入力
hour = input('時:')
minute = input('分:')
second = input('秒:')
time = int(hour) * 3600 + int(minute) * 60 + int(second)
# タイマーを実行する
down_timer.down_timer(time)
