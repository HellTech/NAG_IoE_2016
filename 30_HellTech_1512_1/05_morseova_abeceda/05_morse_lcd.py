#!/usr/bin/python
# -*- coding: utf-8 -*-

import lcddriver
from time import *
import os


lcd = lcddriver.lcd()

line1 = "SOS strojni a elektrotechnicka Velesin"
line2 = "www.sosvel.cz   "


def get_CPU_used():
  with os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'") as cpu:
  	for line in cpu:
  		pass
  	return line.strip()+"%"

def get_RAM_used():
  with os.popen("free") as ram:
  	i=0
  	for line in ram:
  		i+=1
  		if i==2:
  			data=line.split()[1:4]
  			return (str(format(100-float(data[1])/float(data[0])*100, '.1f')+"%"))

def get_CPU_temp():
  with os.popen('vcgencmd measure_temp') as temp:
  	for line in temp:
  		pass
  	return line.split('temp=')[1].split()[0]

def main():
  global line1
  global line2
  str_pad = " " * 16
  str_pad2 = " " * 1
  string1 = str_pad + line1+str_pad2
  lcd.lcd_clear();
  while True:
	  cycle = 0
	  for i in range (0, len(string1)):
	    if cycle>=17:
	      cycle = 0
	    cycle += 1
	    lcd.lcd_display_string(string1[i:(i+15)],1)
	    if cycle>8:
	      lcd.lcd_display_string("CPU"+get_CPU_used()+" RAM"+get_RAM_used(), 2)
	      sleep(0.2)
	    else:
	      lcd.lcd_display_string(line2, 2)
	      sleep(0.4)


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd.lcd_clear();
    lcd.lcd_display_string("Goodbye", 1)
