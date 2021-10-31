#!/bin/bash
cd ~/mini_remote_rpi/playlists/
/usr/bin/vlc --random --loop --fullscreen --audio --volume-step 256 --no-volume-save $1