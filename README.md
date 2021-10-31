# mini_remote_rpi
Mini Remote Control to Start / Stop video show on Raspberry PI

That is a quick and dirty flask micro webservice to start / stop my Halloween video show on an Rasberry PI.
In the background VLC with an predefined playlist will be started. 
You can start the show with or without sound.

## Installation

Everything runs under the default pi User because this user is per default logged on and has the screen session.

### Install basic packages

```
apt install python3 python3-virtualenv python3-pip vlc git nginx screen
```

### Clone the project
```
cd ~
git clone https://github.com/lanbugs/mini_remote_rpi
```

### Create virtualenv and install dependencies
```
cd ~/mini_remote_rpi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Copy systemd service file and enable service

```
sudo cp src/mini_remote_rpi.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable --now mini_remote_rpi.service
```

### Modify settings.ini

Here you can change your playlist which you want to use. 
The playlists are in the ~/mini_remote_rpi/playlists folder.

```
[general]
playlist = example.xspf
```

### Copy nginx config
```
sudo cp src/nginx_default.conf /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

### Try it :-)

You should now get access to the remote control if you use your webbrowser http://<fqdn_ip_of_your_rpi>

Enjoy it ..
