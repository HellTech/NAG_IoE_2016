#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Spust me jako sudo python3 vlakna.py

import sys, threading, time
import RPi.GPIO as GPIO

LED_M = 7 #Modra
LED_B = 8 #Bila
LED_C = 16 #Cervena
LED_Zl = 12 #Zluta
LED_Ze = 32 #Zelena
LED_RGB_R = 18 #RGB_R
LED_RGB_G = 22 #RGB_G
LED_RGB_B = 40 #RGB_B

BUTTON_ENABLED = 37 #zap/vyp
BUTTON_NEXT = 33 #dalsi program

enabled = 0
actual_program = 1

class StopThread(StopIteration):
    pass

threading.SystemExit = SystemExit, StopThread

class DoThread(threading.Thread):

    def _bootstrap(self, stop_thread=False):
        def stop():
            nonlocal stop_thread
            stop_thread = True
        self.stop = stop

        def tracer(*_):
            if stop_thread:
                raise StopThread()
            return tracer
        sys.settrace(tracer)
        super()._bootstrap()

def funguje_callback(channel):
        global enabled, th, actual_program
        if enabled == 1:
                th.stop()
                stopAll()
        else:
                nextProgram()
        enabled = int(not enabled)
        print("zapnuto:",enabled)
        print("Program:",actual_program)
        print("")

def next_callback(channel):
        global actual_program, enabled, th
        actual_program += 1
        if actual_program>5:
                actual_program = 1
        nextProgram()
        print("zapnuto:",enabled)
        print("Program:",actual_program)
        print("")

def nextProgram():
    global actual_program, enabled, th
    if enabled == 1:
        th.stop()
    if actual_program == 1:
        print ("ttt")
        th = DoThread(target=led_program_1)
        th.daemon = True
        th.start()
    if actual_program == 2:
            th = DoThread(target=led_program_2)
            th.daemon = True
            th.start()
    if actual_program == 3:
            th = DoThread(target=led_program_3)
            th.daemon = True
            th.start()
    if actual_program == 4:
            th = DoThread(target=led_program_4)
            th.daemon = True
            th.start()
    if actual_program == 5:
            th = DoThread(target=led_program_5)
            th.daemon = True
            th.start()
    print("zapnuto:",enabled)
    print("Program:",actual_program)
    print("")

def stopAll():
        global a, b, c, d, e, fr, fg, fb
        a.stop()
        b.stop()
        c.stop()
        d.stop()
        e.stop()
        fr.stop()
        fg.stop()
        fb.stop()

def led_program_1():
        global actual_program, a, b, c, d, e, fr, fg, fb
        stopAll()
        next_after = 2; #pocet opakovani programu, pote skok na dalsi
        while True:
            time.sleep(0.5)
            for i in range (65):
                    a.start(1)
                    a.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    b.start(1)
                    b.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    c.start(1) 
                    c.ChangeDutyCycle(i)					
                    time.sleep(0.02)
                    d.start(1)
                    d.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    e.start(1)
                    e.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    fr.start(1) 					
                    fr.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    fg.start(1)
                    fg.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    fb.start(1)
                    fb.ChangeDutyCycle(i)
                    time.sleep(0.02)
                    
            for i in range(65):
                    a.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    b.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    c.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    d.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    e.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    fr.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    fg.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
                    fb.ChangeDutyCycle(100-i)
                    time.sleep(0.02)
            stopAll()
                    
            for i in range(0,5): #Modra
                    blink(LED_M)
            for i in range(0,5): #Bila
                    blink(LED_B)
            for i in range(0,5): #Cervena
                    blink(LED_C)
            for i in range(0,5): #Zelena
                    blink(LED_Ze)
            for i in range(0,5): #Zluta
                    blink(LED_Zl)
            for i in range(0,5): #RED
                    blink(LED_RGB_R)
            for i in range(0,5): #GREEN
                    blink(LED_RGB_G)
            for i in range(0,5): #BLUE
                    blink(LED_RGB_B)
            for i in range(0,5): #ALL
                    blink2(LED_M,LED_B,LED_C,LED_Ze,LED_Zl)
            next_after -= 1
            if next_after <=0:
                break
        actual_program += 1
        print("Program:",actual_program)
        print("")
        led_program_2()

def led_program_2():
        global actual_program, a, b, c, d, e, fr, fg, fb
        stopAll()
        next_after = 2;
        while True:
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_M,GPIO.HIGH)
            GPIO.output(LED_C,GPIO.HIGH)
            GPIO.output(LED_Zl,GPIO.HIGH)
            GPIO.output(LED_Ze,GPIO.HIGH)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            for i in range(0,5):
                    blink(LED_B)
            GPIO.output(LED_B,GPIO.LOW)
            for i in range(0,5):
                    blink(LED_M)
            GPIO.output(LED_M,GPIO.LOW)
            for i in range(0,5):
                    blink(LED_C)
            GPIO.output(LED_C,GPIO.LOW)
            for i in range(0,5):
                    blink(LED_Zl)
            GPIO.output(LED_Zl,GPIO.LOW)
            for i in range(0,5):
                    blink(LED_Ze)
            GPIO.output(LED_Ze,GPIO.LOW)
            for i in range(0,5):
                    blink(LED_RGB_R)
            for i in range(0,5):
                    blink(LED_RGB_G)
            for i in range(0,5):
                    blink(LED_RGB_B)
                    

            next_after -= 1
            if next_after <=0:
                break
        actual_program += 1
        print("Program:",actual_program)
        print("")
        led_program_3()


def led_program_3():
        global actual_program, a, b, c, d, e, fr, fg, fb
        stopAll()
        next_after = 2;
        while True:
            for i in range(0,5):
                    blink(LED_B)
            for i in range(0,5):
                    blink(LED_M)
            for i in range(0,5):
                    blink(LED_C)
            for i in range(0,5):
                    blink(LED_Ze)
            for i in range(0,5):
                    blink(LED_Zl)
            next_after -= 1
            if next_after <=0:
                break
        actual_program += 1
        print("Program:",actual_program)
        print("")
        led_program_4()


def led_program_4():
        global actual_program, a, b, c, d, e, fr, fg, fb
        stopAll()
        next_after = 2;
        while True:
            GPIO.output(LED_M,GPIO.HIGH)
            GPIO.output(LED_C,GPIO.HIGH)
            GPIO.output(LED_Ze,GPIO.HIGH)
            GPIO.output(LED_Zl,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            for i in range(0,5):
                    blink(LED_B)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_C,GPIO.HIGH)
            GPIO.output(LED_Ze,GPIO.HIGH)
            GPIO.output(LED_Zl,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            for i in range(0,5):
                    blink(LED_M)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_M,GPIO.HIGH)
            GPIO.output(LED_Ze,GPIO.HIGH)
            GPIO.output(LED_Zl,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            for i in range(0,5):
                    blink(LED_C)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_M,GPIO.HIGH)
            GPIO.output(LED_C,GPIO.HIGH)
            GPIO.output(LED_Zl,GPIO.HIGH)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            for i in range(0,5):
                    blink(LED_Ze)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_M,GPIO.HIGH)
            GPIO.output(LED_C,GPIO.HIGH)
            GPIO.output(LED_Ze,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.HIGH)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            for i in range(0,5):
                    blink(LED_Zl)
            next_after -= 1
            if next_after <=0:
                break
        actual_program += 1
        print("Program:",actual_program)
        print("")
        led_program_5()
            

def led_program_5():
        global actual_program, a, b, c, d, e, fr, fg, fb
        stopAll()
        next_after = 2;
        while True:
            GPIO.output(LED_M,GPIO.LOW)
            GPIO.output(LED_B,GPIO.LOW)
            GPIO.output(LED_C,GPIO.LOW)
            GPIO.output(LED_Ze,GPIO.LOW)
            GPIO.output(LED_Zl,GPIO.LOW)
            GPIO.output(LED_RGB_R,GPIO.HIGH)
            GPIO.output(LED_RGB_B,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_M,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_C,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_Ze,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_Zl,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_B,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_M,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_B,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_C,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_Ze,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_Zl,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_M,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_C,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_Ze,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_Zl,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_B,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_M,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_B,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_C,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_Ze,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_Zl,GPIO.LOW)
            
            next_after -= 1
            if next_after <=0:
                break
        actual_program = 1
        print("Program:",actual_program)
        print("")
        led_program_1()
            

def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.3)
        return

def blink2(pin,pin2,pin3,pin4,pin5):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.HIGH)
    GPIO.output(pin5,GPIO.HIGH)
    #GPIO.output(pin6,GPIO.HIGH)
    #GPIO.output(pin7,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    #GPIO.output(pin6,GPIO.LOW)
    #GPIO.output(pin7,GPIO.LOW)
    time.sleep(0.1)
    return

def main():
        global enabled, actual_program, th, a, b, c, d, e, fr, fg, fb 
        print("PROGRAM VANOCNI OZDOBA")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setup(LED_B, GPIO.OUT) #Bila
        GPIO.setup(LED_M, GPIO.OUT) #Modra
        GPIO.setup(LED_C, GPIO.OUT) #Cervena
        GPIO.setup(LED_Zl, GPIO.OUT) #Zluta
        GPIO.setup(LED_Ze, GPIO.OUT) #Zelena
        GPIO.setup(LED_RGB_R, GPIO.OUT) #RGB_R
        GPIO.setup(LED_RGB_G, GPIO.OUT)#RGB_G
        GPIO.setup(LED_RGB_B, GPIO.OUT)#RGB_B
        GPIO.setup(BUTTON_ENABLED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        a = GPIO.PWM(LED_B,50)        #Modra
        a.start(0)
        b = GPIO.PWM(LED_M,50)        #Bila
        b.start(0)
        c = GPIO.PWM(LED_C,50)        #Cervena
        c.start(0)
        d = GPIO.PWM(LED_Zl,50)        #Zelena
        d.start(0)
        e = GPIO.PWM(LED_Ze,50)        #Zluta
        e.start(0)
        fr = GPIO.PWM(LED_RGB_R,50)        #RED
        fr.start(0)
        fg = GPIO.PWM(LED_RGB_G,50)        #GREEN
        fg.start(0)
        fb = GPIO.PWM(LED_RGB_B,50)        #BLUE
        fb.start(0)
        GPIO.add_event_detect(BUTTON_ENABLED,GPIO.RISING,callback=funguje_callback,bouncetime=300)
        GPIO.add_event_detect(BUTTON_NEXT,GPIO.RISING,callback=next_callback,bouncetime=300)
        try:
                th = DoThread(target=led_program_1)
                while True:
                        time.sleep(0.5)

        except KeyboardInterrupt:
                pass                   
        stopAll()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print
    print("\nkonec programu")
    GPIO.cleanup()
