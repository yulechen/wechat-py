#!/usr/bin/env bash
python main.py 8081 1>nohup 2>&1 &
echo "server started."