# -*- coding: utf-8 -*-
import requests

def getUrl(url,payload):
    r= requests.get(url, params=payload)
    return r.content

def postUrl(url,payload):
    r = requests.post(url, data=payload)
    return r.content

if __name__ == '__main__':
    print getUrl("https://douban.fm/j/v2/songlist/469032/?kbps=19",None)