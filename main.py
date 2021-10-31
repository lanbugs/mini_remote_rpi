#!/usr/bin/env python3

from flask import Flask, render_template, redirect
import os
from configparser import ConfigParser
import pathlib

BASE_PATH = pathlib.Path(__file__).parent.resolve()

config = ConfigParser()
config.read(os.path.join(BASE_PATH, "etc/settings.ini"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/q/<what>")
def quest(what):

    v = {}

    if what == "start":
        v['what']=what
        v['name']="Start?"

    elif what == "start_sound":
        v['what']=what
        v['name']="Start with sound?"

    elif what == "kill":
        v['what']=what
        v['name']="Kill?"

    elif what == "reboot":
        v['what']=what
        v['name']="Restart?"

    else:
        return redirect("/", code=302)

    return render_template("q.html", v=v)


@app.route("/e/<what>")
def execute(what):

    if what == "start":
        os.system("/usr/bin/screen -dmS video /home/pi/mini_remote_rpi/bin/start_show.sh {}".format(config.get('general', 'playlist')))
    elif what == "start_sound":
        os.system("/usr/bin/screen -dmS video /home/pi/mini_remote_rpi/bin/start_show_with_sound.sh {}".format(config.get('general', 'playlist')))
    elif what == "kill":
        os.system("/usr/bin/screen -X -S video kill")
    elif what == "reboot":
        os.system("/usr/bin/sudo /usr/sbin/reboot")

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run("0.0.0.0")
