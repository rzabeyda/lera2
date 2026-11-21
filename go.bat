@echo off
cd /d C:\lera2
(
echo ---- start
ssh -o BatchMode=yes root@84.200.33.70 "mkdir -p /var/www/kompasskool/img; cd /var/www/kompasskool/img; curl -sfL -o hero.jpg 'https://images.pexels.com/photos/18999540/pexels-photo-18999540.jpeg?auto=compress&cs=tinysrgb&w=1600' && echo ok_hero; chmod 644 *.jpg; ls -la"
scp -o BatchMode=yes index.html root@84.200.33.70:/var/www/kompasskool/index.html && echo SCP_OK
echo ---- end
) > log.txt 2>&1
