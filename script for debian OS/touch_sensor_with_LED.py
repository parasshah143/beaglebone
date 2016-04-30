 #!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time
sensor_pin = 'P8_12'
GPIO.setup(sensor_pin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup("P8_14", GPIO.OUT)
while True:
	print(GPIO.input(sensor_pin))
	if GPIO.input("P8_12") == 1:
		GPIO.output("P8_14", GPIO.HIGH)
		print("Touch")
	else:
		GPIO.output("P8_14", GPIO.LOW)
		print("No Touch")
	time.sleep(0.2)