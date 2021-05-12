## README

Todo:
- historical_hkd - update daily rate as a cron

To run as python3

[development environment only]
pip install -r requirements.txt
python3 sats.py

[production environment only]
WSGI and NGINX Setup
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04


[Yaml Files]
config.yml - url with api key - user needs to add this
rates.yml  - hourly rates from exchange api, autogenerated

[WSGI config]
satshkd.ini
wsgi.py

[system processes]
systemctl status satshkd
satshkd.service

systemctl status satscron
python3 cron.py
