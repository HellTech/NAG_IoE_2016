# Ultrasonic sensor HC-SR04

![HC-SR04](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/10_ultrasonic_sensor_HC-SR04/image/HCSR04.jpg =50x)

<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/10_ultrasonic_sensor_HC-SR04/image/HCSR04.jpg" alt="Drawing" style="width:20px;height:20px" />

Tento návod ukazuje použití Ultrasonic sensor HC-SR04 s [Raspberry Pi](https://www.raspberrypi.org/) pomocí programovacího jazyka [Python](https://www.python.org/).

### Výrobce
Informace na webu výrobce: http://www.micropik.com/PDF/HCSR04.pdf

### Princip funkce
![princip](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/10_ultrasonic_sensor_HC-SR04/image/ultrasonic_sensor_schema.jpg)

### Použité součástky
- [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/model-b-plus/)
- [Ultrasonic sensor HC-SR04](http://www.micropik.com/PDF/HCSR04.pdf)
- I2C LCD displej 2x16 znaků, 1602
- [Adafruit TCA9548A 1-to-8 I2C multiplexer](https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/overview)
- drátové propojky

### Schéma zapojení

![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/10_ultrasonic_sensor_HC-SR04/10_deska.png)

![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/10_ultrasonic_sensor_HC-SR04/10_schem.png)

### Návod k použití
1. Zapojte obvod dle schématu
2. Ujistěte se, že máte zapnutou I2C sběrnici. 
 * [Návod na zprovoznění].(https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/01_lcd_displej)
 * Zkontrolujte zda byla připojená I2C zařízení detekována pomocí příkazu:

   ```
   sudo i2cdetect -y 1
   ```
   Adresa detekovaného LCD displeje by měla být 0x3F.
3. Spusťte program pomocí příkazu

   ```
   sudo python 10_ultrasonic.py
   ```
4. Program ukončete stiskem [CTRL]+[C]

### Ukázka použití

![preview](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/10_ultrasonic_sensor_HC-SR04/image/preview.jpg)

