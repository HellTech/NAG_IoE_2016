#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

BUTTON_PIN=40

def main():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  GPIO.cleanup()
  GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  print "Program Button Pull-UP"
  print "Stiskni tlačítko"
  while True:
    GPIO.wait_for_edge(BUTTON_PIN, GPIO.FALLING)
    print "Tlačítko stisknuto"
    time.sleep(0.8)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
    print
    print "Program ukončen"
    GPIO.cleanup()