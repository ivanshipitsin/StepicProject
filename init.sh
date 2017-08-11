sudo gunicorn -b 0.0.0.0:8080 hello:app
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
