#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import lcddriver
import time

mylcd = lcddriver.lcd()

def find_sensors(basedir):
    return [x for x in os.listdir(basedir) if x.startswith('28')]

def read_temp(sensor):
    with open(sensor + '/w1_slave', "r") as f:
        data = f.readlines()

    if data[0].strip()[-3:] == "YES":
        return [True, float(data[1].split("=")[1])]
    else:
        return [False, 0.0]


if __name__ == "__main__":

    basedir = '/sys/bus/w1/devices'

    sensors = find_sensors(basedir)

    if not sensors:
        print "Teploměr nenalezen"
        sys.exit(0)

    for s in sensors:
        (ok, temp) = read_temp(basedir + '/' + s)

        if ok:
            mylcd.lcd_display_string("Teplota " + str(temp / 1000.0) + " C" ,1)
            mylcd.lcd_display_string("www.sosvel.cz" ,2)
            print "Teplota: "+ str(temp / 1000.0) + " C"
        else:
            print s, ": Teploměr není připraven"
        time.sleep(10)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    mylcd.lcd_clear();
    mylcd.lcd_display_string("Pekny den preje", 1)
    mylcd.lcd_display_string(" *  HellTech  * ", 2)
