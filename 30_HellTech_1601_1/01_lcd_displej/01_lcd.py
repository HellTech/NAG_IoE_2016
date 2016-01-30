#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lcddriver
import time
import datetime

lcd = lcddriver.lcd()
line1 = "SOS strojni a elektrotechnicka Velesin "
line2 = "www.sosvel.cz   "

def main():
  global line1
  global line2  
  str_pad = " " * 16  
  string1 = str_pad + line1
  cycle = 0 
  for i in range (0, len(string1)):  
    if cycle>=11:
      cycle = 0
    cycle += 1
    lcd.lcd_display_string(string1[i:(i+15)],1)  
    if cycle>5:
      
      lcd.lcd_display_string("Datum "+datetime.datetime.now().strftime("%d.").lstrip('0')+datetime.datetime.now().strftime("%m.").lstrip('0')+datetime.datetime.now().strftime("%Y"), 2)
      time.sleep(0.3)
    else:
      lcd.lcd_display_string(line2, 2)
      time.sleep(0.3)
    time.sleep(0.1)
lcd.lcd_clear();

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd.lcd_clear();
    lcd.lcd_display_string("Pekny den preje", 1)
    lcd.lcd_display_string(" *  HellTech  * ", 2)
