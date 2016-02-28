# Krokový motor 28BYJ-48 a řadič ULN2003N

<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/09_step_motor_28BYJ-48_controler_ULN2003N/image/step_motor.jpg" alt="Krokový motor 28BYJ-48" width="300" style="width:300px;" />
<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/09_step_motor_28BYJ-48_controler_ULN2003N/image/controler.jpg" alt="řadič ULN2003N" width="300" style="width:300px;" />
<img src="https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/09_step_motor_28BYJ-48_controler_ULN2003N/image/step_motor_controler.PNG" alt="Krokový motor 28BYJ-48 a řadič ULN2003N" width="300" style="width:300px;" />

Tento návod ukazuje použití tepelného a vlhkostního čidla DHT22 s [Raspberry Pi](https://www.raspberrypi.org/) pomocí programovacího jazyka [Python](https://www.python.org/).

### Výrobce
Informace na webu výrobce:
- http://robocraft.ru/files/datasheet/28BYJ-48.pdf
- http://www.ti.com/lit/ds/symlink/uln2003a.pdf

### Použité součástky
- [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/model-b-plus/)
- [Krokový motor 28BYJ-48](http://robocraft.ru/files/datasheet/28BYJ-48.pdf)
- [Řadič ULN2003N](http://www.ti.com/lit/ds/symlink/uln2003a.pdf)
- drátové propojky

### Schéma zapojení

![Schema1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/09_step_motor_28BYJ-48_controler_ULN2003N/09_deska.png)

![Schema2](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/09_step_motor_28BYJ-48_controler_ULN2003N/09_schem.png)

### Návod k použití
1. Zapojte obvod dle schématu. 
   - Nemějte připojená jiná zařízení, aby nedošlo k přetížení proudového odběru Raspberry. 
   - Pokud máte k dispozici externí zdroj napájení použijte raději jej. Napojte jej na VCC a GND řadiče. Propojte GND externího zdroje a Raspberry.
3. Spusťte program pomocí příkazu

   ```
   09_step_motor.py
   ```
   
   Hřídel motoru se pomalu otáčí.
4. Program ukončete stiskem [CTRL]+[C]

### Ukázka použití

![preview1](https://github.com/HellTech/NAG_IoE_2016/blob/master/30_HellTech_1602_1/09_step_motor_28BYJ-48_controler_ULN2003N/image/preview.jpg)
