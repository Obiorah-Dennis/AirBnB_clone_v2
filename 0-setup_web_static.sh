#!/usr/bin/env bash
# script to configure in order to serve the static pages
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
# instructions
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Fake content
  </body>
</html>" > /data/web_static/releases/test/index.html
# symbolic link to folder erase
ln -sf /data/web_static/releases/test/ /data/web_static/current
# change owner and group to ubuntu
chown -R ubuntu:ubuntu /data/
# change content of available-default
sed -i '43i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t autoindex on;\n\t}\n' /etc/nginx/sites-available/default
# getting changes
service nginx restart
exit 0
