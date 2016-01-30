#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

BUTTON_PIN=40

def stisknuto_callback(channel):
  print "Tlačítko bylo stisknuto"

def main():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.cleanup()
  GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  print "Tlačítko Pull-UP (event_detect)"
  print "program ukončete [CTRL]+[C]"
  print "Stiskni tlačítko"
  GPIO.add_event_detect(BUTTON_PIN,GPIO.RISING,callback=stisknuto_callback,bouncetime=300)
  while True:
    time.sleep(1)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
    print
    print "Program ukončen"
