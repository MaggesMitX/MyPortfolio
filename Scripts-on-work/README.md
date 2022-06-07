Das programm kann als Servive automatisch gestartet werden oder auch als normale Python3 Datei.
System Service commands:
journalctl -u bootup.service Einsicht in die aktuellen Arbeitswerte des services
sudo systemctl status/start/disable/enable/stop bootup.service
unter /etc/systemd/system werden die services abgespeichert.
Für die bootup.service braucht man keine .Sh Dateien.

Auf dem Pi muss im Verzeichnis /home/pi/Dokumente ein ordner mit Python erstellt werden, damit der path übereinstimmt.
Endpath sollte: /home/pi/Dokumente/Python/application.py , sein.
