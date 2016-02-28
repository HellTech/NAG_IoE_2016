# Modul ESP8266 ESP-01

### Výrobce
https://www.adafruit.com/products/2282

### Použité součástky
Modul ESP-01, ESP8266 ze soutěžní sady. Drátové propojky. 

Zapojení
- GND: libovolný gpio kontakt GND
- VCC: libovolný gpio kontakt +3,3 V
- CH_PD: 3,3 V
- TXD: GPIO 15
- RXD: GPIO 14

![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/01_deska.png)

![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/01_ESP8266_ESP-01/01_schem.png)


### Návod
1.	Zapojte obvod dle schématu.
2.	Editujte soubor /etc/inittab pomocí příkazu sudo nano /etc/inittab a vložte znak # na začátek řádků začínajích T0:23:respawn:/sbin/getty
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
Příkaz vypíše informace o nainstalovaném firmwaru v esp modulu. Přehled dalších příkazů
 je k dispozici na http://wiki.iteadstudio.com/ESP8266_Serial_WIFI_Module
8.	Terminál Picocom se ukončuje klávesovou zkratkou [CTRL]+[Q]+[A].
9.	Řešení případných problémů.
    - Zkontrolujte zapojení.
    - Pokud terminál Picocom nereaguje, zkuste odpojit a připojit napájení ESP modulu.
    - Zkuste změnit přenosovou rychlost z 115200 bps na 9600 bps.
    - Rychlost udává parametr –b v příkazu.
    - Pokud nic nepomáhá, nastavte pomocí nástoje sudo raspi-config, sběrnice I2C, serial a ISP na disable.

