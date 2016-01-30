#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from random import randint

def main():
    #pole vsech pouzitych pinu
    pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.cleanup()

    #nastaveni pinu
    for i in range(0,26):
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i],GPIO.LOW)
    
    print "Vánoční ozdoba 2 (had)"
    print "program ukončete [CTRL]+[C]"
    while True:
        print("1/7: postupne rozsviceni")
        for i in range(0,26):
            GPIO.output(pins[i],GPIO.HIGH)
            time.sleep(0.1)
        time.sleep(0.5)
        print("2/7: postupne zhasnuti")
        for i in range(0,26):
            GPIO.output(pins[25-i],GPIO.LOW)
            time.sleep(0.1)
        time.sleep(0.5)
        print("3/7: rozsveceni po dvojicich od konce do stredu")
        for i in range(0,14):
            GPIO.output(pins[i],GPIO.HIGH)
            GPIO.output(pins[25-i],GPIO.HIGH)
            time.sleep(0.1)
        time.sleep(0.5)
        print("4/7: zhasnuti po dvojicich od stredu do konce")
        for i in range(0,13):
            GPIO.output(pins[13+i],GPIO.LOW)
            GPIO.output(pins[13-i],GPIO.LOW)
            time.sleep(0.1)
        time.sleep(0.5)
        print("5/7: rozsviceni jedne led od zacatku do konce")
        for i in range(0,26):
            GPIO.output(pins[i],GPIO.HIGH)
            if i>0:
                GPIO.output(pins[i-1],GPIO.LOW)
            time.sleep(0.1)
        time.sleep(0.5)
        print("6/7: rozsviceni led od konce do zacatku")
        for i in range(0,26):
            GPIO.output(pins[i],GPIO.HIGH)
            if 25>i:
                GPIO.output(pins[i+1],GPIO.LOW)
            time.sleep(0.1)
        time.sleep(0.5)
        print("7/7: náhodné rozvěcení a zhasínání")
        for i in range(0,100):
            for j in range(0,randint(0,26)):
                GPIO.output(pins[j],randint(0,1))
            time.sleep(0.1)

        #zhasni vse
        for i in range(0,26):
            GPIO.output(pins[i],GPIO.LOW)

        print("")


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print
    print("\nkonec programu")
    GPIO.output(3,GPIO.LOW)
    GPIO.cleanup()
