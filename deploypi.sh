#!/usr/bin/env bash
#ssh pi@192.168.3.33 "sudo chmod -R 777 /data/wechat"
scp  baidu* pi@192.168.3.33:~/data/wechat
#scp  startup.sh pi@192.168.3.33:/data/wechat
#scp requirements.txt pi@192.168.3.33:/data/wechat
