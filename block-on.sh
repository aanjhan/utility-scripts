STARTTIME=`date +%R`
STOPTIME=`date -d "$1 minutes" +%R`
sudo iptables -F
echo `sudo iptables -A INPUT -p tcp -m time -s www.facebook.com --timestart $STARTTIME --timestop $STOPTIME -j DROP`
