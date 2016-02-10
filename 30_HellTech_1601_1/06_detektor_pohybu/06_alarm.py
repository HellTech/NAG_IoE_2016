#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import datetime, os, time, sys
from threading import Timer

#settings
PIR_PIN = 25
PASSWORD = "12345"
PATH_ALARM = "alarm.mp3"
START_ALARM_AFTER = 10 #sekundy
TIME_TO_INPUT_CODE = 30 #sekundy
EMAIL_USER = "example@example.com"
EMAIL_PASSWORD = "12345"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

#variables
alarm_enabled = True

def alarm_timer(*args):
  global TIME_TO_INPUT_CODE, PATH_ALARM, EMAIL_USER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, alarm_enabled
  try:
    while TIME_TO_INPUT_CODE>0:
      if not alarm_enabled:
        break      
      time.sleep(1)
      TIME_TO_INPUT_CODE = TIME_TO_INPUT_CODE - 1
    print "Bezpečnostní kód nezadán včas."
    send_email(EMAIL_USER, EMAIL_PASSWORD, EMAIL_USER, "POPLACH", "POPLACH "+getNowStr(), SMTP_SERVER, SMTP_PORT)
    while True:
      if not alarm_enabled:
        break
      print "POPLACH"
      os.popen("omxplayer -o local "+PATH_ALARM)
      time.sleep(0.5)        
  except:
    pass

def getNowStr():
  result = ""
  try:
    result = str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))    
  finally:
    return result

def send_email(user, pwd, recipient, subject, body, smtp_server, smtp_port):
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        #email send ok
    except:
        pass

if __name__ == "__main__":
  try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print "Alarm\n--------------"
    print "Alarm se spustí za " + str(START_ALARM_AFTER) + " sekund."
    time.sleep(START_ALARM_AFTER)
    while True:
      print "Alarm spuštěn."
      while not GPIO.input(PIR_PIN):
        time.sleep(1)
      print "Detekován pohyb."
      Timer(1, alarm_timer, ()).start()
      while alarm_enabled:
        data = raw_input("Zadejte deaktivační kód: ")
        if data == PASSWORD:
           alarm_enabled = False
           break
        print "Zadaný kód není správný."
      print
      while not alarm_enabled:
        data = raw_input("Zadejte aktivační kód: ")
        if data == PASSWORD:
           alarm_enabled = True
           break
        print "Zadaný kód není správný."          
      time.sleep(1)
  except KeyboardInterrupt:
		pass
  finally:
    alarm_enabled = False
    GPIO.cleanup()
    print
    print "konec programu"
    print
    sys.exit(0)
