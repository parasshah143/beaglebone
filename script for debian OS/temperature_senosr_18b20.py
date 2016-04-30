 #!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import time
sensor_pin = 'P9_38'
ADC.setup()
fo = open("foo.txt", "a+")
while True:
	reading = ADC.read(sensor_pin)
	print('\n 1) Temperature sensor value is %f' %reading)
	millivolts = reading * 1800 # 1.8V reference = 1800 mV
	print('  2) millivolt = %d ' % (millivolts))
	digital = (((millivolts*4096)/1800)/14)
	print('   3) digital value is %d' % digital)
	localtime = time.asctime( time.localtime(time.time()) )
	fo.write(' \n Temperature sensor value is %f  Millivolts is %d Digital value is %d  at '  % (reading, millivolts, digital) )
	fo.write(localtime)
	time.sleep(1)