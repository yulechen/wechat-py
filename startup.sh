#!/usr/bin/env bash
PID=$(ps -ef |grep 'main.py' |grep -v 'grep'|awk '{printf $2}')

kill -9 ${PID}
echo "" > nohup
python main.py 8081 1>nohup 2>&1 &
echo "server started."