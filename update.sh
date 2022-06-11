
sudo touch /var/opt/api/tmp
sudo rm -r /var/opt/api/*

sudo cp -r /tmp/api.ozeliurs.com/www/* /var/opt/api/

sudo pip install -r /var/opt/api/requirements.txt

sudo chown -R www-data /var/opt/api/

sudo rm /etc/systemd/system/api.ozeliurs.com.service
sudo cp /tmp/api.ozeliurs.com/api.ozeliurs.com.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart api.ozeliurs.com.service

sudo rm -r /tmp/api.ozeliurs.com