#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P8_10", GPIO.OUT)
while True:
    GPIO.output("P8_10", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P8_10", GPIO.LOW)
    time.sleep(0.5)

	GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(0.5)
	
	GPIO.output("P8_14", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P8_14", GPIO.LOW)
    time.sleep(0.5)
	
	GPIO.output("P8_16", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P8_16", GPIO.LOW)
    time.sleep(0.5)
	