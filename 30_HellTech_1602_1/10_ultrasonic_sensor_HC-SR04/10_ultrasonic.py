#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import RPi_I2C_driver

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
mylcd = RPi_I2C_driver.lcd()
print "Probíhá měření vzdálenosti."
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Čekám na sensor"
time.sleep(2)
while True:
  time.sleep(1)
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  
  while GPIO.input(ECHO)==0:
  	pulse_start = time.time()
  
  while GPIO.input(ECHO)==1:
  	pulse_end = time.time()
  
  pulse_duration = pulse_end - pulse_start
  
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  
  print "Vzdalenost: ",distance," cm"
  mylcd.lcd_display_string("Vzdalenost: ",1)
  mylcd.lcd_display_string(str(distance)+ " cm    " ,2)
GPIO.cleanup()
