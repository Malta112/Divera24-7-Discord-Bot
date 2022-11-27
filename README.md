# Divera24-7-Discord-Bot
Ein Discord bot welcher den Divera24/7 Monitor steuern kann über discord.

![51021169](https://user-images.githubusercontent.com/51021169/204151101-443b70ff-2684-4c66-a841-b69dbe674528.png)

<h1>1.Was ist das?</h1>
Dieser Discord Bot ersetzt die .divera_script.py Datei (https://github.com/Dustin1358/Raspberry-Pi-Divera-Monitor).
Dieser Bot kann dann zu einem Privaten Server hinzugefügt werden. Wer die Richtige Rolle besitzt (WIrd in Installation erklärt)
kann die Befehle benutzen:
<h2>1.1.Hilfe:</h2>
  Zeigt ein Hilfemenu aller Befehle An.
<h2>1.2.Monitor an/aus:</h2>
  Startet beziehungsweise beendet die Anzeige auf dem Display.
<h2>1.3.Neustart:</h2>
  Startet den Raspberry pi neu.
<h2>1.4.Update:</h2>
  Startet ein manuelles Update des Raspberry pi's und startet ihn neu
<h2>1.5.Bildschirmfoto:</h2>
  Erstellt und schickt ein Bildschirmfoto in einen vorher festgelegten Channel,
  Sehr gut um zu schauen ob der Raspi noch läuft und kann aus der Ferne 
  durchgeführt werden
<h2> Gerne Weiter Kommand-Ideen mir schicken</h2>

<h1>2.Installation</h1>



``` 
sudo apt install jq unclutter cec-utils
```
Installiere jq unclutter und cec-tilils. xscreensaver wird noch nicht unterstützt, da noch kein Support für einen Bewegungsmelder existiert.

```
nano divera_commands.sh
```
Öffne die divera_commands.sh (Füge sie in /home/pi ein) und füge deinen Divera autologin key in den dafür vorgesehenen slot ein. (File von Dustin1358)
Die Datei hat keinen .davor mehr, da sie dadurch sichtbar ist und nicht unsichtbar.

```
nano .bashrc
```
öffne die bashrc und füge ganz am ende folgenden ein:
```
source divera_commands.sh
```
Wenn du das getan hast kannst du bashrc neu laden:
```
. ~/.bashrc
```
dannach solltest du einfach 
```
monitor on
```
und 
```
monitor off
```
ausführen können.
Dannach kannst du die Diveracord.py datei auch in /home/pi packen und auch sie bearbeiten mit:
```
nano Diveracord.py
```
Für den Bottoken erstellen empfele ich dir diese Anleitung
```
https://www.ionos.de/digitalguide/server/knowhow/discord-bot-erstellen/
```
Ohner ander.
Wenn du deinen Token eingesetzt hast musst du auf deinem Privaten Server nur noch auf einen Channel 
rechts klicken (Developeroptionen An) und auf ID kopieren gehen.
Diese ID setzt du dann bei Channel ID ein.
Jetzt kannst du noch deinen Kommand prefix setzten also ob es jetzt $help oder !help
heißt (Tipp lass ihn einfach so) und du kannst autoupdate einstellen. Dies heißt
Dass der MOnitor Täglich einen Update macht und dannach neu startet (Auch hier mein Tipp einfach
so lassen)
Dann erstellst und gehst du in einen neuen Ordner für den Autostart:
```
cd .config
mkdir -p ./lxsession/LXDE-pi
touch ./lxsession/LXDE-pi/autostart
nano ./lxsession/LXDE-pi/autostart
```
In der Datei gibst du ein:
```
# remove the next three diamonds to use the desktop again
#@lxpanel --profile LXDE-pi
#@pcmanfm --desktop --profile LXDE-pi
#point-rpi
# start screensaver
#@xscreensaver -no-splash
# stops displaying mouse after five seconds without moving
@unclutter -display :0 -noevents - grab
# does not allow the raspberry to go to sleep
@xset s off
@xset s noblank
@xset -dpms
#starts script
./Diveracord.py
```
<h2>Das war die installation von Diveracord</2>
Ich verweise nochmal auf https://github.com/Dustin1358/Raspberry-Pi-Divera-Monitor Der eigentlich Bot ist selbst
entstanden. Von der Commands.sh wurde nur der Name verändert.
