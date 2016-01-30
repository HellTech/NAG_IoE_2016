#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os

reset='\033[0m'
disable='\033[02m'
red='\033[31m'
green='\033[32m'
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO_PIR = 7
GPIO_R = 27
GPIO_G = 17
 
GPIO.setup(GPIO_G,GPIO.OUT)
GPIO.setup(GPIO_R,GPIO.OUT)
GPIO.output(GPIO_G,GPIO.HIGH)
GPIO.output(GPIO_R,GPIO.LOW)
os.system('clear')
print "Pohybové čidlo (vypnutí CTRL-C)"
GPIO.setup(GPIO_PIR,GPIO.IN)     
Current_State  = 0
Previous_State = 0
try:
  print "Čekám na pohyb..."
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    
  print green+"  Čekám"
  GPIO.output(GPIO_G,GPIO.HIGH)
  GPIO.output(GPIO_R,GPIO.LOW)        
  while True :
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State==1 and Previous_State==0:
      print red+"  Detekován pohyb!"
      GPIO.output(GPIO_G,GPIO.LOW)
      GPIO.output(GPIO_R,GPIO.HIGH)
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      print green+"  Čekám"
      GPIO.output(GPIO_G,GPIO.HIGH)
      GPIO.output(GPIO_R,GPIO.LOW)
      Previous_State=0      
except KeyboardInterrupt:
  print disable+reset+"  Program ukončen" 
  GPIO.cleanup()
