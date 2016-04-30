 #!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
sensor_pin1 = 'P8_11' #touch sensor input
GPIO.setup(sensor_pin1, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup("P8_14", GPIO.OUT)
sensor_pin2 = 'P9_40' #LDR sensor Input
ADC.setup()
fo = open("foo.txt", "a+")
while True:
	#LDR sensor program 
	reading = ADC.read(sensor_pin2)
	#print('\n 1) LDR sensor value is %f' %reading)
	millivolts = reading * 1800 # 1.8V reference = 1800 mV
	#print('  2) millivolt = %d ' % (millivolts))
	digital = (millivolts*4096)/1800
	print('digital value is %d' % digital)
	localtime = time.asctime( time.localtime(time.time()) )
	fo.write(' \n LDR sensor value is %f  Millivolts is %d Digital value is %d at '  % (reading, millivolts, digital) )
	fo.write(localtime)
	time.sleep(0.7)
	#capacitive touch sensor program
	print(GPIO.input(sensor_pin1))
	if (GPIO.input(sensor_pin1) == 1 and digital <= 2000):
		GPIO.output("P8_14", GPIO.HIGH)
		print("Touch")
		fo.write('\n touch')
	else:
		GPIO.output("P8_14", GPIO.LOW)
		print("No Touch")
		fo.write('\n No touch')
	time.sleep(0.7)