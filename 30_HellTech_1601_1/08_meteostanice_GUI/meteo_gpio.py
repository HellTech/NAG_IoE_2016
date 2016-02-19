#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, time, datetime, os
import RPi.GPIO as GPIO
import ds18b20driver
import dht11driver
import bh1750fvidriver
#import meteo_gpio
#from meteo_gpio import *

#config
DHT11_PIN = 14
PIR_PIN = 25

#variables
temperature = 0
humidity = 0
light = 0

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
#GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=lcd_backlight_reset, bouncetime=500)
os.popen("sudo i2cset -y -r  1 0x70 0xff")

def readTemperature():
	global temperature
	try:
		basedir = '/sys/bus/w1/devices'
		sensors = ds18b20driver.find_sensors(basedir)
		if not sensors:
			#print "senzor ds18b20 nedetekován"
			return True
		for s in sensors:
			(ok, temp) = ds18b20driver.read_temp(basedir + '/' + s)
			if ok:
				temperature = float("{0:.2f}".format(temp / 1000.0))
				break
	except:
		pass
		
def readHumidity():
	global DHT11_PIN, humidity
	try:
		count = 0
		while True:
		  dht11var = dht11driver.DHT11(pin = DHT11_PIN)
		  result = dht11var.read()
		  if result.is_valid():
			humidity = int(result.humidity)
			#print "Vlhkost "+str(humidity) + " %" + ", teplota " + str(result.temperature) + " °C"
			break
		  count += 1
		  if count>10:
			#print "Vlhkost - neúspěšné měření"
			break
		  time.sleep(1)
	except:
		pass

def readLight():
	global light
	try:
		light = bh1750fvidriver.readLight()
	except:
		pass

