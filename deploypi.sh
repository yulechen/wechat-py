#!/usr/bin/env bash
#ssh pi@192.168.3.33 "sudo chmod -R 777 /data/wechat"
scp  *.py pi@192.168.3.33:~/data/wechat
#scp  startup* pi@192.168.3.33:~/data/wechat
ssh pi@192.168.3.33 "cd ~/data/wechat && sh startup.sh"
#scp  startup.sh pi@192.168.3.33:/data/wechat
#scp requirements.txt pi@192.168.3.33:/data/wechat
