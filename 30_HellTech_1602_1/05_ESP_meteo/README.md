###Návod

Použité součástky

Modul ESP-01 ze soutěžní sady. Drátové propojky. Čidla ds18b20 a DHT11. 2x odpor 4K7 Ω, odpor 

10K Ω. Solární nabíječka.

obr. 5: schéma zapojení ESP-01 s ds18b20 a DHT11, napájené solární nabíječkou

Návod

a. Zapojte obvod dle schématu.

b. Postupujte jako v předchozím úkolu. Vyplňte v souboru init.lua údaje k WiFi síti. V souboru 

ukol5.lua upravte na řádce 1 proměnou secretid a vyplňte ID Vašeho soutěžního týmu. Nahrajte 

soubory do ESP modulu.
```
./luatool.py --port /dev/ttyAMA0 --src init.lua –dest init.lua –verbose

./luatool.py --port /dev/ttyAMA0 --src ukol5.lua –dest ukol5.lua –verbose
```
c. Restartujte modul node.restart()

d. Ve webovém prohlížeči otevřete přidělenou IP adresu. Ve výpisu je vidět aktuální naměřená 

teplota a vlhkost.

