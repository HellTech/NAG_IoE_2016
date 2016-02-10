import time
import datetime
import os, sys
import RPi.GPIO as GPIO
import dht11driver
import RPi_I2C_driver

mylcd = RPi_I2C_driver.lcd()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PIR_PIN = 25
GPIO.setup(PIR_PIN, GPIO.IN)
PATH_ALARM = "Alarm.mp3"
GPIO.setup(PIR_PIN, GPIO.IN)

instance = dht11driver.DHT11(pin = 14)

def find_sensors(basedir):
    return [x for x in os.listdir(basedir) if x.startswith('28')]


def read_temp(sensor):
    with open(sensor + '/w1_slave', "r") as f:
        data = f.readlines()

    if data[0].strip()[-3:] == "YES":
        return [True, float(data[1].split("=")[1])]
    else:
        return [False, 0.0]

try:
        mylcd.backlight(0)
	print "PIR Module Test (CTRL+C to exit)"
	time.sleep(2)
	print "Ready"
	while True:
		if GPIO.input(PIR_PIN):
			if __name__ == "__main__":

                            basedir = '/sys/bus/w1/devices'

                            sensors = find_sensors(basedir)

                            if not sensors:
                                    print "Teplomer nenalezen"
                                    sys.exit(0)

                            for s in sensors:
                                (ok, temp) = read_temp(basedir + '/' + s)

                                if ok:
                                    mylcd.lcd_display_string("Teplota: " + str(temp / 1000.0) + "C" ,1)
                                    print "Teplota namerena"
                                else:
                                    print s, ": Teplomer neni pripraven"



                        while True:
                            result = instance.read()
                            if result.is_valid():
                                print "Vlhkost namerena"
                                mylcd.lcd_display_string("Vlhkost: " + str("%d%%" % result.humidity) ,2)
                                break

                        time.sleep(10)
                        mylcd.lcd_clear()
                        mylcd.backlight(0)
except KeyboardInterrupt:
	print " Quit"
	GPIO.cleanup()
