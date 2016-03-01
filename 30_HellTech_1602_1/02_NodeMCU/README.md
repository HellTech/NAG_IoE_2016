#Nahrání fimware
NodeMCU je alternativní open-source firmware. Používající programovací jazyk Lua.

a. Stáhněte bin soubor s firmwarem z https://github.com/nodemcu/nodemcu-firmware/releases

Námi použitý bin soubor, jsme přibalili do zdrojových kódů.

b. Pro nahrání nového firmware nainstalujte nástroj esptool.py pomocí příkazů
```
sudo apt-get update

sudo apt-get install git

git clone https://github.com/themadinventor/esptool.git
```

c. Instalaci nového firmware neprovádějte, pokud nemáte ověřenou funkčnost propojení s ESP 

modulem z úkolu 1. Pokud je spuštěný ukončete terminál Picocom. Odpojte ESP modul od 

napájení. Připojte libovolný gpio GND pin na GPIO 0 ESP modulu. Připojte zpět napájení 

modulu.
```
cd esptool

python esptool.py -p /dev/ttyAMA0 write_flash 0x00000 nodemcu_float_0.9.5_20150318.bin
```
d. Pokud dopadla instalace úspěšně. Odpojte modul od napájení. Odpojte pin GPIO 0 a připojte 

napájení modulu.

e. Spusťte terminál 
```
Picocom sudo picocom -b 9600 /dev/ttyAMA0
```
f. Stiskněte [ENTER], objeví se znak > a do terminálu bude možné psát. Zadejte příkaz node.info()

pro vypsání informací o verzi NodeMCU. Dokumentace k NodeMCU příkazům je na 

http://www.nodemcu.com/docs/index/

 

