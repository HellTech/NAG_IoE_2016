#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, datetime, time, os, sys
import RPi.GPIO as GPIO
import ds18b20driver
import dht11driver
import lcddriver
import bh1750fvidriver
from threading import Event, Thread

#settings
DHT11_PIN = 14
PIR_PIN = 25
lcd_turn_on_time = 5
secret_id = "AAA111BBB222"
temperature_urls_list = ["https://api.thingspeak.com/update?api_key=A4B7DNDGM61G09LR&field1={}"]
humidity_urls_list = ["https://api.thingspeak.com/update?api_key=A4B7DNDGM61G09LR&field2={}"]
both_urls_list = ["http://ioe.zcu.cz/th.php?id="+secret_id+"&temperature={}&humidity={}",
                  "http://helltechteam.4fan.cz/weather_rc.php?id=AAxdrtzhedfsdafasf468&temperature={}&humidity={}",
                  "https://script.google.com/macros/s/AKfycbzCzMqdhOhU62EtsNpcgzUwCAzSlGkFSoEtYPm3FC02ymRybso/exec?TEMP_EXT={}&HUMIDITY={}"]
light_urls_list = ["https://api.thingspeak.com/update?api_key=A4B7DNDGM61G09LR&field1={}"]                   
report_speed_data = 60  #sekundy; jak casto odesilat data na servery
update_speed = 30 #sekundy; jak casto aktualizovat data ze senzoru

#variables
temperature = 0.0
humidity = 0.0
light = 0.0
lcd_time = lcd_turn_on_time
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
    lcd_display_string("Teplota "+str(temperature)+" °C   ", 1)
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

def update_light(*args):
  global timer_running, light
  try:
    if not timer_running:
		  return False
    count = 0
    while True:
      light = bh1750fvidriver.readLight()
      print getNowStr() + "Intenzita osvětlení "+str(light) + " lux"
      lcd_display_string("Intenzita osvětlení "+str(light)+" %   ", 2)
      if light:
        break
      count += 1
      if count>10:
        print getNowStr() + "Intenzita osvětlení - neúspěšné měření"
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

def send_light():
  global timer_running, light_urls_list, light
  try:
    if not timer_running:
		  return False
    num_error = 0 
    for url in light_urls_list:
      try:
        f = urllib2.urlopen(url.format(str(light)))
        result_data = f.read().rstrip()
        f.close()
      except:
        print getNowStr() + "Odeslání intenzity osvětlení se nezdařilo -> " + url[:20] + "..."
        num_error += 1
    if num_error == 0:
      print getNowStr() + "Intenzita osvětlení - odeslána OK"
    else:
      print getNowStr() + "Intenzita osvětlení - počet chyb: " + str(num_error)  
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

def lcd_backlight_reset(channel):
  global timer_running, lcd_time, lcd_turn_on_time
  lcd_time = lcd_turn_on_time
  print getNowStr() + "Detekován pohyb, zapnout LCD displej"

def update_lcd_time(*args):
  global timer_running, lcd_time, lcd
  try:
    if not timer_running:
      return True
    if lcd_time>0:
      lcd_time = lcd_time - 1
      #turn on backlight lcd display
      lcd.lcd_backlight_on()
    else:
      #turn off backlight lcd display
      lcd.lcd_backlight_off()
  except:
    return timer_running

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
    # enable i2c multiplexer
    os.popen("sudo i2cset -y -r  1 0x70 0xff")
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=lcd_backlight_reset, bouncetime=500)
    init_lcd_display()
    #first read senzor data
    update_temperature()
    dht11var = dht11driver.DHT11(pin = DHT11_PIN)
    update_humidity()
    update_light()
    #Timer for senzors
    stop_update_temperature = call_repeatedly(update_speed, update_temperature, ())
    stop_update_humidity = call_repeatedly(update_speed, update_humidity, ())
    stop_update_light = call_repeatedly(update_speed, update_light, ())
    #Timer for LCD
    stop_update_lcd_time = call_repeatedly(1, update_lcd_time, ())
    while True:
      send_temperature()
      send_humidity()
      send_light()
      send_both()  
      time.sleep(report_speed_data)
  except KeyboardInterrupt:
		pass
  finally:
    timer_running = False
    stop_update_temperature()
    stop_update_humidity()
    stop_update_light()
    stop_update_lcd_time()
    GPIO.cleanup()
    print
    print getNowStr() + "konec programu"
    lcd_display_string("Pekny den preje", 1, True)
    lcd_display_string(" *  HellTech  * ", 2)
    print
