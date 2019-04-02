#! /usr/local/bin/python3
#  utf-8
import time

def down_timer(max_time):
    for i in range(max_time, 0, -1):  
        print(f"remaining: {i}sec")
        time.sleep(1)
        print("\033[1A", end='')
    #TODO 音をつける
    print("A timer finished!")




