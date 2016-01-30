#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO  
import time


# blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.3)
  
GPIO.setwarnings(False)
GPIO.cleanup()

print "Blikání LED"
try:  
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    for i in range(0,10):
      blink(7)
      blink(8)
    
except KeyboardInterrupt:  
    pass  
finally:  
    GPIO.cleanup()
    print "\nKonec programu\n"
