# -*- coding: utf-8 -*-
#import os
import subprocess
from threading import Lock

player = None
lock = Lock()

def play(url):
    global player
    #os.system('mpg123 "%s"' % url)
    with lock:
        if player != None:
             player.kill()
        player = subprocess.Popen(['mpg123', url])

def stopAll():
    sh = """
     PID=$(ps -ef |grep 'mpg123' |grep -v 'grep' |awk '{printf $2}') && kill -9 ${PID}
    """
    #os.system(sh)
    with lock:
       player.kill()

if __name__ == '__main__':
    stopAll();
