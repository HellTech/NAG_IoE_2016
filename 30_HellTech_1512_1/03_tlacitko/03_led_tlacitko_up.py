#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,0)

print "Tlačítko pull-up"
print "Program ukonči stiskem [CTRL]+[C]"
try:
	while True:
		GPIO.output(7, GPIO.input(11))

except KeyboardInterrupt:  
    pass  
finally:  
    GPIO.cleanup()
    print "\nKonec programu\n"
