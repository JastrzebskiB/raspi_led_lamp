# This is a README.
## Hi!

This is a remotely controlled, Raspberry Pi powered LED lamp.
A lot of shit is hardcoded at the moment and the whole thing is rough around the
edges as hell.
But I just wanted to get it to work, so I'm fine with that.

## Running the server in background
export HOST=raspi.url.on.lan
screen
cd directory/with/project
sudo python3 manage.py runserver 0.0.0.0:8000
[ctrl] + [a], then [d]

## Updating the server
screen -r
[ctrl] + [c]
git pull origin master
pip3 install -r requirements.txt
sudo python3 manage.py runserver 0.0.0.0:8000
[ctrl] + [a], then [d]
