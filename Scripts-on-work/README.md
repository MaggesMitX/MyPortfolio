Das programm kann als Servive automatisch gestartet werden oder auch als normale Python3 Datei.
System Service commands:
journalctl -u bootup.service Einsicht in die aktuellen Arbeitswerte des services
Für eine genaue Filterung des fehlers kann mit dem Befehl "sudo journalctl -f -u xxx.service" der Fehler ausgegeben werden
sudo systemctl status/start/disable/enable/stop bootup.service
unter /etc/systemd/system werden die services abgespeichert.

Erweiterte Hilfestellung ist verlinkt:
https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f

https://wiki.archlinux.org/title/systemd

Auf dem Pi muss im Verzeichnis /home/pi/Dokumente ein ordner mit Python erstellt werden, damit der path übereinstimmt.
Endpath sollte: /home/pi/Dokumente/Python/application.py , sein.
