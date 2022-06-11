
sudo touch /opt/api/tmp
sudo rm -r /opt/api/*

sudo cp -r /tmp/api.ozeliurs.com/www/* /opt/api/

sudo pip install -r /opt/api/requirements.txt

sudo chown -R www-data /opt/api/

sudo rm /etc/systemd/system/api.ozeliurs.com.service
sudo cp /tmp/api.ozeliurs.com/api.ozeliurs.com.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart api.ozeliurs.com.service

sudo rm -r /tmp/api.ozeliurs.com