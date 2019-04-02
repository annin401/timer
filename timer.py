#! /usr/local/bin/python3
# timer.py
#  utf-8

import time
import sys
import down_timer

max_time = 0

#python3から呼び出すときと，コマンドのようにでも呼び出せるようにする
#TODO 正規表現で書き換える
if sys.argv[0] == "python3":
    max_time = int(sys.argv[2])
elif sys.argv[0] == "timer.py":
    max_time = int(sys.argv[1])

down_timer.down_timer(max_time)





