#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import lcddriver
import tcs34725driver
import RPi.GPIO as GPIO

if __name__ == "__main__":
  lcd = None
  try:
    print "RGB COLOR SENSOR TCS34725"
    # initialize
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    os.popen("sudo i2cset -y -r  1 0x70 0x3f 0x29")
    lcd = lcddriver.lcd()
    lcd.lcd_clear();
    lcd.lcd_display_string("RGB ...", 1) 
    while True:
      ok, r, g, b = tcs34725driver.readColor()
      print "R: %s, G: %s, B: %s" % (r, g, b)
      lcd.lcd_display_string("R: %s G:%s        " % (r,g), 1)
      lcd.lcd_display_string("B: %s  " % (b), 2)
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
 