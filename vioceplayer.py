# -*- coding: utf-8 -*-
#import os
import subprocess

player = None

def play(url):
    global player
    #os.system('mpg123 "%s"' % url)
    player = subprocess.Popen(['mpg123', url])

def stopAll():
    sh = """
     PID=$(ps -ef |grep 'mpg123' |grep -v 'grep' |awk '{printf $2}') && kill -9 ${PID}
    """
    #os.system(sh)
    player.kill()

if __name__ == '__main__':
    stopAll();
