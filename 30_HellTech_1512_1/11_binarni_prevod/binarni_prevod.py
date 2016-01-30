#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import lcddriver
from time import *

LED1 = 35
LED2 = 33
LED3 = 31
LED4 = 29
BUTTON1 = 40
BUTTON2 = 38
BUTTON3 = 36
BUTTON4 = 37

message1 = "BINARNI PREVOD"
LED1_enable = 0
LED2_enable = 0
LED3_enable = 0
LED4_enable = 0

GPIO.setwarnings(False)
lcd = lcddriver.lcd()

def button1_callback(channel):
  global LED1_enable
  LED1_enable = int(not LED1_enable)
  GPIO.output(LED1,LED1_enable)
  recalculate()

def button2_callback(channel):
  global LED2_enable
  LED2_enable = int(not LED2_enable)
  GPIO.output(LED2,LED2_enable)
  recalculate()

def button3_callback(channel):
  global LED3_enable
  LED3_enable = int(not LED3_enable)
  GPIO.output(LED3,LED3_enable)
  recalculate()  

def button4_callback(channel):
  global LED4_enable
  LED4_enable = int(not LED4_enable)
  GPIO.output(LED4,LED4_enable)
  recalculate()

def recalculate():
  global lcd
  global LED1_enable, LED2_enable, LED3_enable, LED4_enable 
  bin = str(LED1_enable) + str(LED2_enable) + str(LED3_enable) + str(LED4_enable)
  dec = str(int(bin, 2))
  message2 = "BIN "+bin + " DEC "+ dec + "  "
  print message2
  lcd.lcd_display_string(message2, 2)
    
  
def main():
  global lcd
  global message1, LED1_enable, LED2_enable, LED3_enable, LED4_enable
   
  print message1
  print "www.sosvel.cz"
  print "(pro přerušení programu stiskni [CTRL]+[C])"
  print
  lcd.lcd_clear()
  lcd.lcd_display_string(message1, 1)
  lcd.lcd_display_string("www.sosvel.cz", 2)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  GPIO.setup(LED1, GPIO.OUT)
  GPIO.setup(LED2, GPIO.OUT)
  GPIO.setup(LED3, GPIO.OUT)
  GPIO.setup(LED4, GPIO.OUT)
  GPIO.output(LED1,LED1_enable)
  GPIO.output(LED2,LED2_enable)
  GPIO.output(LED3,LED3_enable)
  GPIO.output(LED4,LED4_enable)
  GPIO.setup(BUTTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.setup(BUTTON2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.setup(BUTTON3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.setup(BUTTON4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback=button1_callback, bouncetime=300)
  GPIO.add_event_detect(BUTTON2, GPIO.RISING, callback=button2_callback, bouncetime=300)
  GPIO.add_event_detect(BUTTON3, GPIO.RISING, callback=button3_callback, bouncetime=300)
  GPIO.add_event_detect(BUTTON4, GPIO.RISING, callback=button4_callback, bouncetime=300)
  recalculate()  
  while True:
    sleep(50)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
    print
    print "konec programu"
    lcd.lcd_clear()
    lcd.lcd_display_string("KONEC PROGRAMU", 1)
