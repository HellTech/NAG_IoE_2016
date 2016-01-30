#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import dht11driver
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11driver.DHT11(pin = 12)

while True:
  result = instance.read()
  if result.is_valid():
    print("Čas měření: " + str(datetime.datetime.now()))
    print("Teplota: %d C" % result.temperature)
    print("Vlhkost: %d %%" % result.humidity)
    break
  time.sleep(1)
