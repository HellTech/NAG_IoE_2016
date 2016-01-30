#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import os, re, urllib
#from time import *
import time
import sys
from sys import stdout

LED_PIN=7
MORSE_DOT = 0.2
MORSE_DASH = 0.5
MORSE_LETTER_PAUSE = 0.2
MORSE_WORD_PAUSE = 0.5
PATH_DOT = 'morse_dot.ogg'
PATH_DASH = 'morse_dash.ogg'

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

morseAlphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "Ä"	: ".-.-",
    "Á"	: ".--.-",
    "Å"	: ".--.-",
    "Ch"	: "----",
    "É"	: "..-..",
    "Ñ"	: "--.--",
    "Ö"	: "---.",
    "Ü"	: "..--",
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    " " : "/",
    "." : ".-.-.-",
    ":" : "---...",
    '_': '..--.-',
    ';': '-.-.-.',
    '?': '..--..',
    "'": '.----.',
    '(': '-.--.-',
    ')': '-.--.-',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.'
    }

inverseMorseAlphabet = {}
for key, val in morseAlphabet.items(): inverseMorseAlphabet[val] = key

morse_data = ''
morse_message = ''

def morse_encode(text):
    return ' '.join(map(lambda x, g=morseAlphabet.get: g(x, '*'), text.upper()))

def morse_decode(message):
    ans = ''.join(map(lambda x, g=inverseMorseAlphabet.get: g(x, '*'), message.split(' ')))
    return ' '.join(ans.split())


def morse_led_dot():
	GPIO.output(7,1)
	os.popen("omxplayer -o local "+PATH_DOT)
	time.sleep(0.2)
	GPIO.output(7,0)
	time.sleep(0.2)
	'''
	morse_led_high()
	#os.popen("omxplayer -o local "+PATH_DOT)
	time.sleep(MORSE_DOT)
	morse_led_low()
	time.sleep(MORSE_LETTER_PAUSE)
	'''

def morse_led_dash():
	GPIO.output(7,1)
	os.popen("omxplayer -o local "+PATH_DASH)
	time.sleep(0.5)
	GPIO.output(7,0)
	time.sleep(0.2)
	'''
	morse_led_high()
	#os.popen("omxplayer -o local "+PATH_DASH)
	time.sleep(MORSE_DASH)
	morse_led_low()
	time.sleep(MORSE_LETTER_PAUSE)
	'''
def morse_led_low():
	GPIO.output(LED_PIN,0)

def morse_led_high():
	GPIO.output(LED_PIN,1)
  
def print_in_same_place(text=''):
  stdout.write("\r%s" % text)
  stdout.flush()
  
def print_in_same_place_close_line():
  stdout.write("\n")
  
def print_back_up_line():
  sys.stdout.write("\033[F")
  
def print_led_update(symbol,position,position_letter):
  global morse_data
  global morse_message
  os.system('clear')
  print RED+"Morseova abeceda"+END
  print "-----------------------"
  print BLUE+"Zpráva se zobrazuje na LED:"+END
  print GREEN+symbol+END
  print
  print BLUE+"Přijatá data:"+END
  print PURPLE+morse_data[:position]+GREEN+UNDERLINE+morse_data[position:position+1]+END+PURPLE+morse_data[position+1:]+END
  print
  print BLUE+"Dešifrovaná zpráva:"+END
  print YELLOW+morse_message[:position_letter]+END
    
def main():
  global morse_data
  global morse_message
  os.system('clear')
  print RED+"Morseova abeceda"+END
  print "-----------------------"
  print
  print BLUE+"Stahování dat ze serveru ZCU..."+END
  
  id="mh...Z2"
  f = urllib.urlopen('https://ioe.zcu.cz/morse.php?id='+id)
  morse_data = f.read().rstrip()
  
  if morse_data > 0:
    print GREEN+"OK"+END
  else:
    print RED+"Error"+END  
  
  print
  print BLUE+"Přijatá data:"+END
  print PURPLE+morse_data+END
  print
  print BLUE+"Dešifrovaná zpráva:"+END
  morse_message = morse_decode(morse_data)
  print YELLOW+morse_message+END
  print
  
  raw_input('Signalizovat zprávu pomocí LED a AUDIO výstupu [Enter], přerušit [CTRl]+[C]\n')
  print_back_up_line()
  
  #Morse LED
  LED_PIN=7
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(LED_PIN,GPIO.OUT)
  morse_led_low()
  
  position = 0
  position_letter = 0
  for symbol in morse_data:
    print_led_update(symbol,position,position_letter)
    if symbol == '-':
      morse_led_dash()
    elif symbol == '.':
      morse_led_dot()
    else:
      if symbol == ' ':
        position_letter += 1
      time.sleep(MORSE_WORD_PAUSE)
    position += 1
    stdout.flush()
    time.sleep(MORSE_WORD_PAUSE)
  
  morse_led_low()  
  print_led_update('',position,position_letter+1)
  print
  print GREEN+"Hotovo"+END
  print
  

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.setwarnings(False)
    GPIO.cleanup()
    print
    print "program ukončen"+END
