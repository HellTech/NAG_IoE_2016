#Instalace Led k ESP modulu
###Použité součástky
Modul ESP-01 ze soutěžní sady. Drátové propojky. Dvě LED diody. 2x odpor 220 Ω.
![Schéma](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/03_ESP_LED/03_deska.png)
![Schéma](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/03_ESP_LED/03_schem.png)


###Návod

1. Zapojte obvod dle schématu.

2. Pro nahrání souborů se skripty do ESP modulu nainstalujte nástroj Luatool.
```
git clone https://github.com/4refr0nt/luatool.git

cd luatool
 ```

3. Ze složky úkolu 03 ve zdrojových kódech zkopírujte do složky luatool soubory init.lua

a ukol3.lua.


4. Editujte soubor nano ukol3.lua a vyplňte název SSID a heslo wifi sítě, ke které chcete 

ESP modul připojit.


5. Nahrajte soubory do ESP modulu
```
./luatool.py --port /dev/ttyAMA0 --src init.lua –dest init.lua –verbose

./luatool.py --port /dev/ttyAMA0 --src ukol3.lua –dest ukol3.lua –verbose
```

6. Spuťte Picocom a restartuje modul
```
sudo picocom -b 9600 /dev/ttyAMA0

node.restart()
 ```

7. Po restartu zkontrolujte výpis do terminálu a zjistěte IP adresu přidělenou modulu. IP 

adresu lze zjistit i příkazem 
```
print(wifi.sta.getip())
```

8. Na počítači (atd.) připojeném do stejné WiFi sítě otevřete v prohlížeči zjištěnou 

IP adresu. Pomocí zobrazené webové stránky je možné ovládat připojené LED diody.
