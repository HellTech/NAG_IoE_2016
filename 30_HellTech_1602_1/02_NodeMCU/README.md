#Nahrání fimware
1. Stáhli jsme esptool
2. Stáhli jsme si fimware s této stránky: https://github.com/nodemcu/nodemcu-firmware/releases.
3. Pomocí Příkazu jsme naistalovani fimware.
```  
python esptool.py -p /dev/ttyAMA0 write-flash 0x00000 nodemcu_float_0.9.5-2015 0318.bin 
```
###Komunikace s modulem po nahrání fimware
Nyní musíme komunikovat s modulem rychlostí 9600. 
``` 
picocom-b 9600 --omap crcrlf/dev/ttyAMA0.
```
###Spuštění příkazu
Příkazy spouštíme dofile("nazev souboru")


 

