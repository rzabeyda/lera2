#!/bin/bash
# Run on the server once. Only adds a new nginx site and a new service; other bots are untouched.
set -e
mkdir -p /var/www/kompasskool /opt/lera2
cp /root/lera2-upload/index.html /var/www/kompasskool/
cp -r /root/lera2-upload/docs /var/www/kompasskool/
cp /root/lera2-upload/server.py /opt/lera2/
cp /root/lera2-upload/nginx-kompasskool.conf /etc/nginx/sites-available/kompasskool
ln -sf /etc/nginx/sites-available/kompasskool /etc/nginx/sites-enabled/kompasskool
cp /root/lera2-upload/lera2.service /etc/systemd/system/lera2.service
pip3 install fastapi uvicorn --break-system-packages
systemctl daemon-reload
systemctl enable --now lera2
nginx -t && systemctl reload nginx
echo "OK -> http://kompasskool.ee  (HTTPS: certbot --nginx -d kompasskool.ee -d www.kompasskool.ee)"
