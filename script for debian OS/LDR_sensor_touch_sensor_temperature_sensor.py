 #!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
sensor_pin1 = 'P8_12' #touch sensor input
GPIO.setup(sensor_pin1, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup("P8_14", GPIO.OUT)
sensor_pin2 = 'P9_40' #LDR sensor Input
sensor_pin3 = 'P9_38' #Temperature sensor Input
ADC.setup()
fo = open("foo.txt", "a+")
while True:
	#capacitive touch sensor program
	print(GPIO.input(sensor_pin1))
	if GPIO.input("P8_12") == 1:
		GPIO.output("P8_14", GPIO.HIGH)
		print("Touch")
		fo.write('\n >> touch')
	else:
		GPIO.output("P8_14", GPIO.LOW)
		print("No Touch")
		fo.write('\n >> No touch')
	time.sleep(0.2)
	#LDR sensor program 
	reading1 = ADC.read(sensor_pin2)
	print('\n 1) LDR sensor value is %f' %reading1)
	millivolts1 = reading1 * 1800 # 1.8V reference = 1800 mV
	print('  2) millivolt1 = %d ' % (millivolts1))
	digital1 = (millivolts1*4096)/1800
	print('   3) digital1 value is %d' % digital1)
	localtime = time.asctime( time.localtime(time.time()) )
	fo.write(' \n 1) LDR sensor value is %f  2) Millivolts1 is %d 3) Digital1 value is %d at '  % (reading1, millivolts1, digital1) )
	fo.write(localtime)
	time.sleep(1)
	#temperature sensor 
	reading2 = ADC.read(sensor_pin3)
	print('\n 4) Temperature sensor value is %f' %reading2)
	millivolts2 = reading2 * 1800 # 1.8V reference = 1800 mV
	print('  5) millivolt2 = %d ' % (millivolts2))
	digital2 = (((millivolts2*4096)/1800)/14)
	print('   6) digital value is %d' % digital2)
	localtime = time.asctime( time.localtime(time.time()) )
	fo.write(' \n 4) Temperature sensor value is %f  5) Millivolts2 is %d 6) Digital2 value is %d  at '  % (reading2, millivolts2, digital2) )
	fo.write(localtime)
	time.sleep(1)