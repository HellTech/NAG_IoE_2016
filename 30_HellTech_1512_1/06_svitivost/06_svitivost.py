#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO        
import time

try:
  print "LED PWM"
  print "program ukončete [CTRL]+[C]"
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  GPIO.setup(7, GPIO.OUT) 
  p = GPIO.PWM(7,50)        
  p.start(0)
  while True:
		for i in range (100):
			p.ChangeDutyCycle(i)
			time.sleep(0.02)        
		for i in range(100):
			p.ChangeDutyCycle(100-i)
			time.sleep(0.02)         

except KeyboardInterrupt:
  p.stop()
  pass
finally:
  GPIO.cleanup()
  print
  print "Program ukončen"