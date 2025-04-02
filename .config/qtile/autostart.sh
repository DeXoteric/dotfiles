#!/bin/zsh

# Disable mouse acceleration
for id in $(xinput list | grep "pointer" | cut -d '=' -f 2 | cut -f 1); do
    xinput --set-prop $id 'libinput Accel Profile Enabled' 0, 1
done

# Set wallpaper using feh
feh --bg-fill $HOME/.wallpaper/sakura-gate.jpg &

# Start Picom for transparency and compositing
picom &

# Start Redshift
redshift &

# Opens pajacyk.pl and clicks on the belly
~/python-projects/pajacyk-pl/pajacyk.sh &
