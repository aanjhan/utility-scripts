#! /bin/bash

NUMOFARGS=1
STARTTIME=`date +%R`
STOPTIME=`date -d "$1 minutes" +%R`
blacklist=(www.facebook.com twitter.com linkedin.com)

# Some input sanitisation
if [ $# -ne $NUMOFARGS ]; then
        echo "Usage : Specify the time duration of the block in minutes"
        exit
fi

# Flush iptables
# This works for me since I dont have any iptables rules usually
sudo iptables -F

# Block the blacklisted sites for the prescribed period

for (( i=0;i<${#blacklist[@]};i++)); do
    echo "Blocking ${blacklist[${i}]}..."
    echo `sudo iptables -A OUTPUT -p tcp -m time -d ${blacklist[${i}]} --timestart $STARTTIME --timestop $STOPTIME -j DROP`    
done




