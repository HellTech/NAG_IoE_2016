#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

RGB_RED = 11
RGB_GREEN = 16
RGB_BLUE = 15

BUTTON_RED =  29
BUTTON_GREEN = 31
BUTTON_BLUE = 33

state_red = 0
state_green = 0
state_blue = 0

def red_callback(channel):
  global RGB_RED, state_red
  state_red = int(not state_red)
  print "Tlačítko RED bylo stisknuto, stav: " + str(state_red)
  GPIO.output(RGB_RED,state_red)

def green_callback(channel):
  global RGB_GREEN, state_green
  state_green = int(not state_green)
  print "Tlačítko GREEN bylo stisknuto, stav: " + str(state_green)
  GPIO.output(RGB_GREEN,state_green)

def blue_callback(channel):
  global RGB_BLUE, state_blue
  state_blue = int(not state_blue)
  print "Tlačítko BLUE bylo stisknuto, stav: " + str(state_blue)
  GPIO.output(RGB_BLUE,state_blue)


try:
  print "RGB dioda PWM, tlačítka"
  print "program ukončete [CTRL]+[C]"
  print "Míchejte barvy RGB pomocí tlačítek"
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  
  GPIO.setup(RGB_RED,GPIO.OUT) #RED
  GPIO.output(RGB_RED,state_red)
  GPIO.setup(RGB_GREEN,GPIO.OUT)  #GREEN
  GPIO.output(RGB_GREEN,state_green)
  GPIO.setup(RGB_BLUE,GPIO.OUT)  #BLUE
  GPIO.output(RGB_BLUE,state_blue)
  GPIO.setup(BUTTON_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(BUTTON_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(BUTTON_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.add_event_detect(BUTTON_RED,GPIO.RISING,callback=red_callback,bouncetime=300)
  GPIO.add_event_detect(BUTTON_GREEN,GPIO.RISING,callback=green_callback,bouncetime=300)
  GPIO.add_event_detect(BUTTON_BLUE,GPIO.RISING,callback=blue_callback,bouncetime=300)
  
  while(True):
    time.sleep(1)

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
  print
  print "Program ukončen"