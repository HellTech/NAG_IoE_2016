# Waterproof_DS18B20

<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/06_Waterproof_DS18B20/image/ds18b20waterproof.jpg" alt="Waterproof_DS18B20" width="300" style="width:300px;" />

Tento návod ukazuje použití tepelného čidla Waterproof_DS18B20 s [Raspberry Pi](https://www.raspberrypi.org/) pomocí programovacího jazyka [Python](https://www.python.org/).

### Výrobce
Informace na webu výrobce: https://www.adafruit.com/products/381

### Použité součástky
- [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/model-b-plus/)
- [Waterproof_DS18B20](https://www.adafruit.com/products/381)
- I2C LCD displej 2x16 znaků, 1602
- drátové propojky
- odpor 4K7 Ω

### Schéma zapojení

![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/06_Waterproof_DS18B20/06_deska.png)

![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/06_Waterproof_DS18B20/06_schem.png)

### Návod k použití
1. Zapojte obvod dle schématu
2. Ujistěte se, že máte zapnutou I2C sběrnici. 
 * [Návod na zprovoznění](https://github.com/HellTech/NAG_IoE_2016/tree/master/30_HellTech_1601_1/01_lcd_displej)
 * Zkontrolujte zda byla připojená I2C zařízení detekována pomocí příkazu:

   ```
   sudo i2cdetect -y 1
   ```
   Adresa detekovaného LCD displeje by měla být 0x3F.
3. Spusťte program pomocí příkazu

   ```
   sudo 06_ds18b20.py
   ```
4. Program ukončete stiskem [CTRL]+[C]

### Ukázka použití

Voda ohřátá pomocí varné konvice.
![preview1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/06_Waterproof_DS18B20/image/preview1.jpg)

Naměřená hodnota.
![preview2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/06_Waterproof_DS18B20/image/preview2.jpg)

Teplota vody zchlazené v mrazničce, ale nezamrzlé.
![preview3](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/06_Waterproof_DS18B20/image/preview3.jpg)

