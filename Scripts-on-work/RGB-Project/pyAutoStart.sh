#! /bin/sh
### BEGIN INIT INFO
# Provides: RGB_Printer.py
# Required-Start: $syslog
# Required-Stop: $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start LED/ RGB Application
# Description: Ersell wurde ein python script, welches den 3D Drucker zum leuchten 
#bringen soll, und später aktuelle Statusmeldungen anzeigt
### END INIT INFO
 
case "$1" in
    start)
        echo "RGB Stripe Programm wird gestartet"
        # Starte Programm
        /home/pi/Dokumente/Python/led_animation.py
        ;;
    stop)
        echo "RGB Stripe Programm wird beendet"
        # Beende Programm
        killall led_animation.py
        ;;
    *)
        echo "Benutzt: /home/ta/Dokumente/Python/led_animation.py {start|stop}"
        exit 1
        ;;
esac
 
exit 0