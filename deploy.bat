@echo off
cd /d C:\lera2
ssh root@84.200.33.70 "mkdir -p /root/lera2-upload"
scp -r index.html docs server.py nginx-kompasskool.conf lera2.service setup-server.sh root@84.200.33.70:/root/lera2-upload/
ssh root@84.200.33.70 "bash /root/lera2-upload/setup-server.sh"
pause
