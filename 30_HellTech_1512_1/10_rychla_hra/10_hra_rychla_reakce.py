#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import os
import random
import lcddriver
from time import *

P1_LED = 36
P2_LED = 38
MAIN_LED = 40
P1_BUTTON = 35
P2_BUTTON = 37
RESET_BUTTON = 33

P1_score = 0
P2_score = 0

message1 = "RYCHLA REAKCE"

GPIO.setwarnings(False)
lcd = lcddriver.lcd()

def reset_callback(channel):
    global P1_score
    global P2_score
    global lcd
    P1_score = 0
    P2_score = 0
    message2 = "Body M:"+str(P1_score)+" Z:"+str(P2_score)
    lcd.lcd_display_string(message2+"     ",2)  

def main():
  global P1_score
  global P2_score
  global message1
  global lcd
   
  print message1
  print "www.sosvel.cz"
  print "(pro ukončení hry stiskni [CTRL]+[C])"
  print
  lcd.lcd_clear()
  lcd.lcd_display_string(message1, 1)
  lcd.lcd_display_string("www.sosvel.cz", 2)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  GPIO.setup(MAIN_LED, GPIO.OUT)
  GPIO.setup(P1_LED, GPIO.OUT)
  GPIO.setup(P2_LED, GPIO.OUT)
  GPIO.setup(P1_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.setup(P2_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.setup(RESET_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.add_event_detect(RESET_BUTTON, GPIO.RISING, callback=reset_callback, bouncetime=300)
  GPIO.output(P1_LED,0)
  GPIO.output(P2_LED,0)
  GPIO.output(MAIN_LED,0)
  while True:
    message2 = "Připravit   "
    print message2
    print
    #lcd.lcd_display_string("Pripravit",2)
  
    lcd.lcd_display_string(message1+"  5",1)
    print "5"
    sleep(1.5)
    lcd.lcd_display_string(message1+"  4",1)
    print "4"
    sleep(1.5)  
    lcd.lcd_display_string(message1+"  3",1)
    print "3"
    sleep(1.5)
    lcd.lcd_display_string(message1+"  2",1)
    print "2"
    sleep(1.5)
    lcd.lcd_display_string(message1+"  1",1)
    print "1"
    sleep(1.5)
    lcd.lcd_display_string(message1+"   ",1)
    lcd.lcd_display_string("Hra bezi         ",2)
    print "Hra běží"  
    
    GPIO.output(P1_LED,0)
    GPIO.output(P2_LED,0)
    GPIO.output(MAIN_LED,1)
    sleep(random.uniform(5,10))
    GPIO.output(MAIN_LED,0)
    
    while True:
      if GPIO.input(P1_BUTTON) == False:
        GPIO.output(P1_LED,1)
        P1_score += 1
        break
      if GPIO.input(P2_BUTTON) == False:
        GPIO.output(P2_LED,1)
        P2_score += 1
        break
        
    message2 = "Body M:"+str(P1_score)+" Z:"+str(P2_score)     
    print message2
    print      
    lcd.lcd_display_string(message2, 2)


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.output(P1_LED,0)
    GPIO.output(P2_LED,0)
    GPIO.output(MAIN_LED,0)
    GPIO.cleanup()
    print
    print "konec hry"
    lcd.lcd_clear()
    lcd.lcd_display_string("KONEC HRY", 1)
