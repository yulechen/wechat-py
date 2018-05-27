#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import requestutil
import jsonutil

#0-为你推荐
#2-流行
#2-流行
def getPlayTypeId(typeName):
    #  为你推荐,流行,民谣
  list=jsonutil.toObject(requestutil.getUrl("https://douban.fm/j/v2/songlist/explore/genres",None))
  rdict={};
  for item in list:
      name =item['name']
      id=item['id']
      rdict[name]=id
  return rdict.get(typeName)


def getPlayList(typeId):
    playload={};
    playload['type']='hot'
    playload['genre']=typeId
    playload['limit']=20
    playload['sample_cnt']=5
    list = jsonutil.toObject(requestutil.getUrl("https://douban.fm/j/v2/songlist/explore", playload))
    size = len(list)
    urlIndex = random.randint(0, size-1)
    return list[urlIndex]['id']

def getMp3urls(playlisyId):
    playload = {};
    playload['kbps'] = 192
    url ="https://douban.fm/j/v2/songlist/"+str(playlisyId)+"/"
    #print url
    list = jsonutil.toObject(requestutil.getUrl(url, playload))
    return  list

def getRandomMp3(list):
   size=len(list['songs'])
   urlIndex=random.randint(0, size-1)
   return list['songs'][urlIndex]['url']


def getRecommendedforyou():
   randomePlaylist= getPlayList(0)
   playlistMap3=getMp3urls(randomePlaylist)
   return getRandomMp3(playlistMap3)

if __name__ == '__main__':
#  id= getPlayTypeId(u'为你推荐')
#  playlisyId=getPlayList(id)
  #list = getMp3urls(u'303825')
 # print getRandomMp3(list)
   print getRecommendedforyou()