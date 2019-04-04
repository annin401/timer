#!  /usr/local/bin/python3
#   main.py
#   codeing:UTF-8
import down_timer
import argument_process

# 引数から整数のタプルを生成する
time = argument_process.argument_process()

# タイマーを実行する
down_timer.down_timer(max_time)

