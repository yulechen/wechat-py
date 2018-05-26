#!/usr/bin/python
# coding: utf-8
import httplib
import json
import sys
import subprocess
import time
reload(sys)
sys.setdefaultencoding('utf-8')
while True:
  # 获取播放列表
  httpConnection = httplib.HTTPConnection('douban.fm')
  httpConnection.request('GET', '/j/mine/playlist?type=n&channel=4')
  song = json.loads(httpConnection.getresponse().read())['song']
  picture = 'images/' + song[0]['picture'].split('/')[4]
  # 播放
  player = subprocess.Popen(['mpg123', song[0]['url']])
  time.sleep(song[0]['length'])
  player.kill()

