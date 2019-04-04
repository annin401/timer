#! /usr/local/bin/python3
#  down_timer.py
#  utf-8
#  This file is a part of "timer" made by annin
import time
import sys

def down_timer(max_time):
    for i in range(max_time, 0, -1):  
        print(f"remaining: {i}sec")
        time.sleep(1)
        print("\033[1A", end='')
    #TODO formatを整える
    #TODO 音をつける
    print("A timer finished!")

