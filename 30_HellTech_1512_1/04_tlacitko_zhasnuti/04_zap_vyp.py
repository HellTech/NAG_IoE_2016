#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,0)

sviti = 1

try:
	print "Tlačítko zap/vyp LED diodu"
  print "program ukončete [CTRL]+[C]"
  print "Stiskni tlačítko"
  while True:
		if (GPIO.input(11)== 1):
			GPIO.output(7,sviti)
			if (sviti== 1):
				sviti=0
			else:
				sviti = 1
			time.sleep(0.2) 

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
  print
  print "Program ukončen"