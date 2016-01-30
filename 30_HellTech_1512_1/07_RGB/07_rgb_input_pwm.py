#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

RGB_RED = 11
RGB_GREEN = 16
RGB_BLUE = 15

try:
  print "RGB dioda PWM"
  print "program ukončete [CTRL]+[C]"
  print "Zadej 000-111, například 101 nebo 110 atd."
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  
  GPIO.setup(RGB_RED,GPIO.OUT) #RED
  GPIO.output(RGB_RED,1)
  r = GPIO.PWM(RGB_RED,50)
  GPIO.setup(RGB_GREEN,GPIO.OUT)  #GREEN
  GPIO.output(RGB_GREEN,1)
  g = GPIO.PWM(RGB_GREEN,50)
  GPIO.setup(RGB_BLUE,GPIO.OUT)  #BLUE
  GPIO.output(RGB_BLUE,1)
  b = GPIO.PWM(RGB_BLUE,50)
  while(True):
    request = raw_input("RGB-->")
    if (len(request) == 3):
      GPIO.output(RGB_RED,int(request[0]))
      GPIO.output(RGB_GREEN,int(request[1]))
      GPIO.output(RGB_BLUE,int(request[2]))
      for i in range (100):
        if int(request[0]) == 0:
          r.ChangeDutyCycle(i)
        if int(request[1]) == 0:
          g.ChangeDutyCycle(i)
        if int(request[2]) == 0:
          b.ChangeDutyCycle(i)
        time.sleep(0.02)       
      for i in range(100):
        if int(request[0]) == 0:
          r.ChangeDutyCycle(100-i)
        if int(request[1]) == 0:
          g.ChangeDutyCycle(i)
        if int(request[2]) == 0:
          b.ChangeDutyCycle(i)
        time.sleep(0.02) 

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
  print
  print "Program ukončen"