#!  /usr/local/bin/python3
#   main.py
#   codeing:UTF-8
import down_timer
import timer_sound
import os
import threading

# 非同期処理
flag = True
def wait_input():
    global flag
    input()
    flag = False


#入力
hour = input('hours:')
minute = input('minutes:')
second = input('seconds:')
time = int(hour) * 3600 + int(minute) * 60 + int(second)

# タイマーを実行する
down_timer.down_timer(time)
#終了したら通知センターに通知
os.system("osascript -e 'display notification\"A timer finished!\"'")
#非同期処理開始
th = threading.Thread(target=wait_input)
th.start()
#音楽再生
timer_sound.music_playback()

th.join()
