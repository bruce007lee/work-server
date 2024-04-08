#!/bin/bash
 
# 指定端口号
PORT=5001
 
# 找到占用指定端口的进程ID（PID）
PID=$(sudo lsof -t -i:$PORT)
 
# 检查是否有进程占用该端口
if [ ! -z "$PID" ]; then
    # 杀死占用端口的进程
    sudo kill $PID
    
    # 检查进程是否被成功杀死
    if sudo kill -0 $PID > /dev/null 2>&1; then
        echo "进程 $PID 未能被杀死。"
    else
        echo "进程 $PID 已被杀死。"
    fi
else
    echo "没有发现占用端口 $PORT 的进程。"
fi