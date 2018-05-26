# -*- coding: utf-8 -*-
import os


def voice_text(text):
    print text
    url = "http://tsn.baidu.com/text2audio?tex=" + text + "&lan=zh&per=0&cuid=pi1110&ctp=1&" \
                                                          "tok=24.b4eee1dcf4b3416f990ab9bf960180e3.2592000.1529911294.282335-11302635"

    print url
    os.system('mpg123 "%s"' % url)


if __name__ == '__main__':
    voice_text("你是个好人测试")
