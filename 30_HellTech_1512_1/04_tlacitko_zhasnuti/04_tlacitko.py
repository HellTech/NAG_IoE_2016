#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

try:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  
  GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(7,GPIO.OUT)
  GPIO.output(7,0)
  
  sviti = 0

  print "Tlačítko Pull-Down"
  print "program ukončete [CTRL]+[C]"
  print "Stiskni tlačítko a LED dioda bude 5 sekund svítit"
  
  while True:
		if (GPIO.input(11)== 1):
			GPIO.output(7,1)
			time.sleep(5)
		else:
			GPIO.output(7,0)

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
  print
  print "Program ukončen"
