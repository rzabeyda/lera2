@echo off
cd /d C:\lera2
ssh root@84.200.33.70 "mkdir -p /var/www/kompasskool/img && cd /var/www/kompasskool/img && for f in 0b6a95937895e87a82337694696ed426622c196b 518c95f83555902ce085bc20a1fc8f1c3733982d 916360d0866219ff83d016de0b7c701cf9098e1a d57194bcbf34ed7cc26951ca45f50d5a56d8695e; do curl -sf -o $f.jpg https://prokoolitus.net/img/$f.jpg && echo OK $f || echo FAIL $f; done; chmod 644 *.jpg; ls -la"
scp index.html root@84.200.33.70:/var/www/kompasskool/index.html
echo.
echo GOTOVO
pause
