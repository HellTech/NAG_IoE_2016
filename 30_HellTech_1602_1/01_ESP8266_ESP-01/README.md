# Modul ESP8266 ESP-01

<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/image/esp-01.png" alt="ESP-01" width="300" style="width:300px;" />
<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/image/esp-01_scheme.png" alt="ESP-01 scheme" width="300" style="width:300px;" />

### Výrobce
Informace na webu výrobce: https://www.adafruit.com/products/2282

### Použité součástky
- [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/model-b-plus/)
- [Modul ESP-01](https://www.adafruit.com/products/2282)
- drátové propojky.

### Zapojení
- GND: libovolný gpio kontakt GND
- VCC: libovolný gpio kontakt +3,3 V
- CH_PD: 3,3 V
- TXD: GPIO 15
- RXD: GPIO 14

![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/01_deska.png)

![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/01_schem.png)


### Návod
1.	Zapojte obvod dle schématu.
2.	Editujte soubor /etc/inittab pomocí příkazu

   ```
   sudo nano /etc/inittab
   ```
   a vložte znak # na začátek řádků začínajích 

   ```
   T0:23:respawn:/sbin/getty
   ```
3.	Pro komunikaci s modulem je potřeba nainstalovat terminálový program Picocom.

   ```
sudo aptitude update && sudo aptitude install picocom
   ```
4.  Restartujte Raspberry příkazem 

   ```
   sudo reboot
   ```
5.	Spusťte terminál Picocom příkazem

   ```
   sudo picocom -b 115200 /dev/ttyAMA0 –omap crcrlf
   ```
6.	Stiskněte klávesu [ENTER]. Pokud je vše správně do terminálu bude možné psát.
7.	Zadejte příkaz AT+GMR a potvrďte [ENTER].

   ```
   AT+GMR
   ```
   
   ![Picocom](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/image/picocom.PNG)
   
   Příkaz vypíše informace o nainstalovaném firmwaru v esp modulu. Přehled dalších příkazů je k dispozici na http://wiki.iteadstudio.com/ESP8266_Serial_WIFI_Module
8.	Terminál Picocom se ukončuje klávesovou zkratkou [CTRL]+[Q]+[A].
9.	Řešení případných problémů.
    - Zkontrolujte zapojení.
    - Pokud terminál Picocom nereaguje, zkuste odpojit a připojit napájení ESP modulu.
    - Zkuste změnit přenosovou rychlost z 115200 bps na 9600 bps.
    - Rychlost udává parametr –b v příkazu.
    - Pokud nic nepomáhá, nastavte pomocí nástoje sudo raspi-config, sběrnice I2C, serial a ISP na disable.
    
    ![raspi-config](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/image/raspi-config.png) 

