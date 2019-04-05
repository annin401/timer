#   python3
#   down_timer.py
#   codeing:UTF-8
import time

def down_timer(max_time):
    for i in range(max_time, -1, -1):  
        hour = i // 3600
        minute = i %  3600 // 60
        second = i % 60 
        print("remaining: {hour:02}h{minute:02}m{second:02}s"
                .format(hour=hour, minute=minute, second=second))
        time.sleep(1)
        print("\033[1A", end='')
    #TODO formatを整える
    #TODO 音をつける
    print("\nA timer finished!")

