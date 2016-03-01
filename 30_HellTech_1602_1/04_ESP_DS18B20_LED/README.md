###Návod
![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/04_ESP_DS18B20_LED/04_deska.png)
![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/04_ESP_DS18B20_LED/04_schem.png)
a. Zapojte obvod dle schématu.

b. Postupujte jako v předchozím úkolu. Vyplňte v souboru init.lua údaje k WiFi síti. Nahrajte do 

ESP modulu soubory z toho úkolu.
```
./luatool.py --port /dev/ttyAMA0 --src init.lua –dest init.lua –verbose

./luatool.py --port /dev/ttyAMA0 --src ukol4.lua –dest ukol3.lua –verbose
```
c. Restartujte modul node.restart()

d. Ve webovém prohlížeči otevřete přidělenou IP adresu. Ve výpisu je vidět aktuální naměřená 

teplota.

