#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lcddriver
import dht22driver

DHT22_PIN = 14

if __name__ == "__main__":
  lcd = None
  try:
    print "DHT22"
    # initialize
    lcd = lcddriver.lcd()
    lcd.lcd_clear();
    lcd.lcd_display_string("...", 1) 
    while True:
      t, h, ok = dht22driver.read(DHT22_PIN)
      if ok:
          print("Teplota = {0} °C, Vlhkost = {1} %".format(t, h))
          lcd.lcd_display_string("Teplota: " + str(t) + " *C", 1)
          lcd.lcd_display_string("Vlhkost: " + str(h) + " %", 2)
      else:
          print("Chyba senzoru.")
      time.sleep(1)
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
    print
    print "konec programu"
    lcd.lcd_display_string("Pekny den preje", 1)
    lcd.lcd_display_string(" *  HellTech  * ", 2)
    print
 






