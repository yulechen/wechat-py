# -*- coding: utf-8 -*-
from threading import Thread

import vioceplayer
import db
import baiduvoice

def async(f):
    def wrapper(*args):
        thr = Thread(target = f, args = args)
        thr.start()
    return wrapper

@async
def doMsgAync(msg):
    url = ""#baiduvoice.text2audio(msg)
    #vioceplayer.play(url)
    if 'music' in msg  or  '歌' in msg or '音乐' in msg:
       url= db.getRecommendedforyou()
    elif msg == "kill" or msg == "关闭":
       vioceplayer.stopAll()
    else:
      url = baiduvoice.text2audio(msg)
    vioceplayer.play(url)


if __name__ == '__main__':
    doMsgAync("music")
