# RGB color sensor TCS34725

![TCS34725](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/11_RGB_color_sensor_TCS34725/image/TCS34725.jpg)

Tento návod ukazuje použití RGB color sensor TCS34725 s [Raspberry Pi](https://www.raspberrypi.org/) pomocí programovacího jazyka [Python](https://www.python.org/).

### Výrobce
Informace na webu výrobce: https://www.adafruit.com/products/1334

### Použité součástky
- [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/model-b-plus/)
- [RGB color sensor TCS34725](https://www.adafruit.com/products/1334)
- I2C LCD displej 2x16 znaků, 1602
- [Adafruit TCA9548A 1-to-8 I2C multiplexer](https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/overview)
- drátové propojky

### Schéma zapojení

![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/11_RGB_color_sensor_TCS34725/11_deska.png)

![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/11_RGB_color_sensor_TCS34725/11_schem.png)

### Návod k použití
1. Zapojte obvod dle schématu
2. Ujistěte se, že máte zapnutou I2C sběrnici. 
 * [Návod na zprovoznění].(https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/01_lcd_displej)
 * Zkontrolujte zda byla připojená I2C zařízení detekována pomocí příkazu:

   ```
   sudo i2cdetect -y 1
   ```
   Adresy detekovaných zařízení by měli být:
   - 0x70 multiplexer
   - 0x3F LCD displej
   - 0x29 RGB TCS34725
3. Spusťte program pomocí příkazu

   ```
   sudo python 11_rgb.py
   ```
4. Program ukončete stiskem [CTRL]+[C]

### Ukázka použití

![preview](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/11_RGB_color_sensor_TCS34725/image/preview.jpg)

