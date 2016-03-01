# Meteostanice GUI v2.01

<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/08_Meteostanice_GUI_v2/image/preview.png" width="300" style="width:300px;" />

Tento návod ukazuje použití a zapojení meteostanice 2 s [Raspberry Pi](https://www.raspberrypi.org/) pomocí programovacího jazyka [Python](https://www.python.org/).

### Meteostanice GUI 1
První verze meteostanice: https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/08_meteostanice_GUI

### Funkce meteostanice 2
- měří vnitřní a venkovní teplotu, vlhkost a osvětlenost
- zobrazuje aktuální předpověď počasí pomocí webu http://openweathermap.org/
- odesílá na naměřená data na zadané servery
- posílá chybové logy na email
- podporuje zobrazení na celou obrazovku
- pohybové čidlo zajišťuje úsporu elektřiny – obrazovka je rozsvícená, jen pokud je detekován pohyb a za okamžik se opět vypne
- meteostanice 2 má více možností nastavení, ukládání do konfiguračního souboru
- větší stabilita aplikace

### Changelog
02/2016, 2.01 - oprava drobných chyb GUI

02/2016, 2.0 - první release

### Použité součástky
- [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/model-b-plus/)
- [Adafruit TCA9548A 1-to-8 I2C multiplexer](https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/overview)
- [Raspberry Pi 7" Touch Display](https://www.raspberrypi.org/products/raspberry-pi-touch-display/)
- [Waterproof_DS18B20](https://www.adafruit.com/products/381)
- [DHT11](https://www.adafruit.com/product/386)
- [DHT22](https://www.adafruit.com/products/385)
- [Light sensor BH1750FVI](http://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/light/bh1750fvi-e.pdf)
- [IR senzor HC-SR501](https://www.mpja.com/download/31227sc.pdf)
- drátové propojky
- 3x odpor 4K7 Ω

### Schéma zapojení

![Schema](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/08_Meteostanice_GUI_v2/08_deska.png)


### Návod k použití
1. Připojte 7" dotykový displej.
   - [Návod od výrobce](https://www.raspberrypi.org/blog/the-eagerly-awaited-raspberry-pi-display/)
   - [Alternativní návod](https://www.element14.com/community/docs/DOC-78156/l/raspberry-pi-7-touchscreen-display)
2. Zapojte obvod dle schématu.

   > Vekovní čidla jsme umístili do krabičky vytištěné na 3D tiskárně pomocí modelu [Vented and shaded box for outdoor temp and humidity sensors](http://www.thingiverse.com/thing:146132).
3. Ujistěte se, že máte zapnutou I2C sběrnici. 
 * [Návod na zprovoznění](https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/01_lcd_displej)
 * Zkontrolujte zda byla připojená I2C zařízení detekována pomocí příkazu:

   ```
   sudo i2cdetect -y 1
   ```
   Adresy detekovaných zařízení by měli být:
   - 0x70 multiplexer
   - 0x23 Light sensor BH1750FVI
4. Nainstalujte GTK

   ```
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install libgtk2.0-dev
   sudo apt-get install libgtk-3-dev
   sudo apt-get install glade
   ```
5. Pokud nemáte spuštěno grafické uživatelské prostředí, spusťte jej příkazem

   ```
   startx
   ```
   >Tip: nastavit režim po spuštění Raspberry (terminál/grafické prostředí) lze pomocí nástroje `sudo raspi-config`
6. Spusťte program pomocí příkazu

   ```
   sudo python meteo.py
   ```
7. Po spuštění programu zkontrolujte nastavení na kartě "Nastavení".
   - upravte adresy serverů, na které chcete odesílat naměřené údaje; uveďte jejich adresy na samostané řádky
   - v url adresách bude automaticky nahrazeno

   ```
   t1 - vnitřní teplota
   h1 - vnitřní vlhkost
   t2 - venkovní teplota
   h2 - venkovní vlhkost
   l - osvětlenost
   ```
   - změňte hodnoty pro přepověď počasí pomocí openweathermap (lokace, appid); appid lze získat registrací na http://openweathermap.org/ 
   - vyplňte email na nějž chcete zasílat chybová hlášení
8. (volitelné) Prohlédněte si náš další projekt "[Zobrazení naměřených údajů na webu](https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/09_meteostanice_web_skoly)".
Údaje naměřené naší meteostanicí jsou k dispozici na http://meteo.sosvel.cz




### Ukázka použití

Meteostanice 2

![preview1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/08_Meteostanice_GUI_v2/image/preview.png)



Web s naměřenými údaji: http://meteo.sosvel.cz

Projekt: https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/09_meteostanice_web_skoly

![preview2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/08_Meteostanice_GUI_v2/image/preview2.png)



Tisk krabičky na 3D tiskárně

![preview3](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/08_Meteostanice_GUI_v2/image/preview3.jpg)



Hotová krabička

![preview4](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/08_Meteostanice_GUI_v2/image/preview4.jpg)

