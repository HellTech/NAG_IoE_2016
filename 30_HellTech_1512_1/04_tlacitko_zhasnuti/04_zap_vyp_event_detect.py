#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

BUTTON_PIN = 11
LED_PIN = 7

def stisknuto_callback(channel):
  global sviti
  sviti = int(not sviti)
  GPIO.output(LED_PIN,sviti)
  if sviti == 1:
    print "LED dioda ZAPNUTA"
  else:
    print "LED dioda VYPNUTA"    

try:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  
  GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(LED_PIN,GPIO.OUT)
  GPIO.output(LED_PIN,0)
  
  sviti = 0

  print "Tlačítko zap/vyp LED diodu"
  print "program ukončete [CTRL]+[C]"
  print "Stiskni tlačítko"
  GPIO.add_event_detect(BUTTON_PIN,GPIO.RISING,callback=stisknuto_callback,bouncetime=300)
  GPIO.output(LED_PIN,sviti)  
  while True:
    time.sleep(1) 

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
  print
  print "Program ukončen"