#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, datetime, time, os, sys
import RPi.GPIO as GPIO
import ds18b20driver
import dht11driver
import lcddriver
from threading import Event, Thread
#from time import *

#settings
DHT11_PIN = 14
secret_id = "AAAbbb"
zcu_url = "http://ioe.zcu.cz/th.php?id="+secret_id+"&temperature={}&humidity={}"
report_speed = 60  #sekundy
update_speed = 30  #sekundy

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

def update_temperature(*args):
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

def update_humidity(*args):
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
		
def send_data():
  global timer_running, zcu_url, temperature, humidity
  try:
    if not timer_running:
		return False
    try:
      f = urllib2.urlopen(zcu_url.format(str(temperature),str(humidity)))
      result_data = f.read().rstrip()
      f.close()
      if "Data ulozena" in result_data:      
        print getNowStr() + "Data odeslána OK."
      else:
        print getNowStr() + "Data se nepodařilo uložit!" 
    except:
      print getNowStr() + "Chyba odeslání dat!"
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

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        while not stopped.wait(interval):
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

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
    stop_update_temperature = call_repeatedly(update_speed, update_temperature, ())
    stop_update_humidity = call_repeatedly(update_speed, update_humidity, ())
    while True:
      send_data()
      time.sleep(report_speed)
  except KeyboardInterrupt:
      pass
  finally:
    timer_running = False
    stop_update_temperature()
    stop_update_humidity()
    GPIO.cleanup()
    print
    print getNowStr() + "konec programu"
    lcd_display_string("Pekny den preje", 1, True)
    lcd_display_string(" *  HellTech  * ", 2)
    print
