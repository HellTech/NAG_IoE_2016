#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
# Definice pinu pro pouzivani
# Fyzicke piny 7,11,13,15
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [ 37 , 35 , 33 , 31 ]
 
# Nastaveni vsech pinu jako output
for pin in StepPins:
   print "Motor pripraven"
   GPIO.setup(pin,GPIO.OUT)
   GPIO.output(pin, False )
 
# Definovani sekvence
Seq = [[ 1 , 0 , 0 , 1 ],
        [ 1 , 0 , 0 , 0 ],
        [ 1 , 1 , 0 , 0 ],
        [ 0 , 1 , 0 , 0 ],
        [ 0 , 1 , 1 , 0 ],
        [ 0 , 0 , 1 , 0 ],
        [ 0 , 0 , 1 , 1 ],
        [ 0 , 0 , 0 , 1 ]]
        
StepCount = len (Seq)
StepDir = 2 # Nastav 1 nebo 2 pro smer podle hod. rucicek
             # Nastav -1 nebo -2 pro smer proti hod. rucickam 
 
# cekani
if len (sys.argv)> 1 :
   WaitTime = int (sys.argv[ 1 ]) / float ( 3000 )
else :
   WaitTime = 10 / float ( 3000 )
 
# Initialise
StepCounter = 0
 
# Start main loop
while True :
#if True: 
   for pin in range ( 0 , 4 ):
     xpin = StepPins[pin] # Get GPIO
     if Seq[StepCounter][pin]!= 0:
       GPIO.output(xpin, True )
     else :
       GPIO.output(xpin, False )
 
   StepCounter += StepDir
 
   # Jestli narazime na konec sekvence
   # zacni znovu
   if (StepCounter >= StepCount):
     StepCounter = 0
   if (StepCounter< 0 ):
     StepCounter = StepCount + StepDir
 
   # Pockej pred pohybem 
   time.sleep(WaitTime)
