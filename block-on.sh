#! /bin/bash

NUMOFARGS=1
STARTTIME=`date +%R`
STOPTIME=`date -d "$1 minutes" +%R`

if [ $# -ne $NUMOFARGS ]; then
        echo "Usage : Missing time argument"
        exit
fi


sudo iptables -F
echo `sudo iptables -A INPUT -p tcp -m time -s www.facebook.com --timestart $STARTTIME --timestop $STOPTIME -j DROP`
