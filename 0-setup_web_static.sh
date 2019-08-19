#!/usr/bin/env bash
# setup server for serving web things
apt-get -y update
apt-get -y install nginx
mkdir --parents /data/web_static/releases/test
mkdir --parents /data/web_static/shared
ln --force --symbolic /data/web_static/releases/test /data/web_static/current
cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
chown --recursive ubuntu:ubuntu /data
cat > /etc/nginx/sites-available/default << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    root /var/www/html;
    index index.html;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
EOF
service nginx reload
service nginx restart
