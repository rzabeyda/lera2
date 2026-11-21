@echo off
ssh root@84.200.33.70 "certbot --nginx -d kompasskool.ee -d www.kompasskool.ee --non-interactive --agree-tos -m admin@kompasskool.ee --redirect"
ssh root@84.200.33.70 "python3 -c \"import sqlite3;c=sqlite3.connect(chr(47)+chr(111)+chr(112)+chr(116)+chr(47)+chr(108)+chr(101)+chr(114)+chr(97)+chr(50)+chr(47)+chr(114)+chr(101)+chr(103)+chr(46)+chr(100)+chr(98));c.execute(chr(100)+chr(101)+chr(108)+chr(101)+chr(116)+chr(101)+chr(32)+chr(102)+chr(114)+chr(111)+chr(109)+chr(32)+chr(114)+chr(101)+chr(103));c.commit()\""
pause
