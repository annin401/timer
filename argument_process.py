#   python3  
#   argument_process.py 
#   coding:UTF-8

import click
import re

@click.command()
@click.argument('time', help="Time you want to set, for example '1h2m0s'")
def argument_process(time):
    # コマンド引数から情報を取り出す
    hours = re.compile(r"\d*h").search(time)
    minutes = re.compile(r"\d*m".search(time)
    seconds = re.compile(r"\d*s".search(time)

    # タイマーは最大24時間以内
    if(24 < hours or 60 < minutes or 60 < seconds):  
        raise click.BadParameter('''
        Enter hours in the range of 0 to 24
              minutes in the range of 0 to 60  
              seconds in the range of 0 to 60
        ''')

    return hours, minutes, seconds


