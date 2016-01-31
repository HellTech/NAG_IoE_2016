#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, datetime, time, os, sys
import RPi.GPIO as GPIO
import ds18b20driver
import dht11driver
import lcddriver
from threading import Timer
#from time import *

#settings
DHT11_PIN = 14
secret_id = "mhBUnLi8Xc6hgswmxaDhebEjBl7DPLZ2"
temperature_urls_list = ["https://api.thingspeak.com/update?api_key=A4B7DNDGM61G09LR&field1={}"]
humidity_urls_list = ["https://api.thingspeak.com/update?api_key=A4B7DNDGM61G09LR&field2={}"]
both_urls_list = ["http://ioe.zcu.cz/th.php?id="+secret_id+"&temperature={}&humidity={}",
                  "http://helltechteam.4fan.cz/weather_rc.php?id=AAxdrtzhedfsdafasf468&temperature={}&humidity={}",
                  "https://script.google.com/macros/s/AKfycbzCzMqdhOhU62EtsNpcgzUwCAzSlGkFSoEtYPm3FC02ymRybso/exec?TEMP_EXT={}&HUMIDITY={}"]
report_speed_ZCU = 3  #sekundy
update_speed = 10 

#global variables
temperature = 0.0
humidity = 0.0
timer_running = True

def getNowStr():
  result = ""
  try:
    result = str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')) + ": "    
  finally:
    return result

def update_temperature():
  global timer_running, temperature
  try:
    if not timer_running:
		return False
    basedir = '/sys/bus/w1/devices'
    sensors = ds18b20driver.find_sensors(basedir)
    if not sensors:
        print getNowStr() + "senzor ds18b20 nedetekován"
        return True
    for s in sensors:
        (ok, temp) = ds18b20driver.read_temp(basedir + '/' + s)
        if ok:
            temperature = float("{0:.2f}".format(temp / 1000.0))
            break
    print getNowStr() + "Teplota "+str(temperature) + " °C"
    lcd_display_string("Teplota "+str(temperature)+" C   ", 1)
  except:
    return timer_running

def update_humidity():
  global timer_running, dht11var, humidity
  try:
    if not timer_running:
		return False
    count = 0
    while True:
      result = dht11var.read()
      if result.is_valid():
        humidity = int(result.humidity)
        print getNowStr() + "Vlhkost "+str(humidity) + " %" + ", teplota " + str(result.temperature) + " °C"
        lcd_display_string("Vlhkost "+str(humidity)+" %   ", 2)
        break
      count += 1
      if count>10:
        print getNowStr() + "Vlhkost - neúspěšné měření"
        break
      time.sleep(1)
  except:
    return timer_running
		
def send_temperature():
  global timer_running, temperature_urls_list, temperature
  try:
    if not timer_running:
		return False
    num_error = 0 
    for url in temperature_urls_list:
      try:
        f = urllib2.urlopen(url.format(str(temperature)))
        result_data = f.read().rstrip()
        f.close()
      except:
        print getNowStr() + "Odeslání teploty se nezdařilo -> " + url[:20] + "..."
        num_error += 1
    if num_error == 0:
      print getNowStr() + "Teplota - odeslána OK"
    else:
      print getNowStr() + "Teplota - počet chyb: " + str(num_error)  
  finally:
    return timer_running

def send_humidity():
  global timer_running, humidity_urls_list, humidity
  try:
    if not timer_running:
		return False
    num_error = 0 
    for url in humidity_urls_list:
      try:
        f = urllib2.urlopen(url.format(str(humidity)))
        result_data = f.read().rstrip()
        f.close()
      except:
        print getNowStr() + "Odeslání vlhkosti se nezdařilo -> " + url[:20] + "..."
        num_error += 1
    if num_error == 0:
      print getNowStr() + "Vlhkost - odeslána OK"
    else:
      print getNowStr() + "Vlhkost - počet chyb: " + str(num_error)  
  finally:
    return timer_running

def send_both():
  global timer_running, both_urls_list, temperature, humidity
  try:
    if not timer_running:
		return False
    num_error = 0 
    for url in both_urls_list:
      try:
        f = urllib2.urlopen(url.format(str(temperature),str(humidity)))
        result_data = f.read().rstrip()
        f.close()
      except:
        print getNowStr() + "Odeslání dat se nezdařilo -> " + url[:20] + "..."
        num_error += 1
    if num_error == 0:
      print getNowStr() + "Data - odeslána OK"
    else:
      print getNowStr() + "Data - počet chyb: " + str(num_error)  
  finally:
    return timer_running

def init_lcd_display():
  global lcd
  try:
    lcd = lcddriver.lcd()
    lcd.lcd_clear();
    lcd.lcd_display_string("Meteo HellTech", 1)    
  except:
    pass 

def lcd_display_string(message,line,clear=False):
  global lcd
  try:
    if clear:
      lcd.lcd_clear()
    lcd.lcd_display_string(message, line)    
  except:
    pass 

if __name__ == "__main__":
  lcd = None
  try:
    print "Meteostanice 30 - HellTech"
    print getNowStr() + "start programu"
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    init_lcd_display()
    #first read senzor data
    update_temperature()
    dht11var = dht11driver.DHT11(pin = DHT11_PIN)
    update_humidity()
    #Timer for senzors
    Timer(update_speed, update_temperature, ()).start()
    Timer(update_speed, update_humidity, ()).start()
    while True:
      send_temperature()
      send_humidity()
      send_both()  
      time.sleep(report_speed_ZCU)
  except KeyboardInterrupt:
      pass
  finally:
    timer_running = False
    GPIO.cleanup()
    print
    print getNowStr() + "konec programu"
    lcd_display_string("Pekny den preje", 1, True)
    lcd_display_string(" *  HellTech  * ", 2)
    print
