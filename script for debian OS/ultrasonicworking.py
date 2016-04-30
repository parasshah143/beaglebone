import Adafruit_BBIO.GPIO as GPIO
import time 
GPIO.setup("P8_16", GPIO.IN) 
GPIO.setup("P8_14", GPIO.OUT) 
print("Start")
while True:
	GPIO.output("P8_14", GPIO.HIGH)
	time.sleep(0.0001)
	GPIO.output("P8_14", GPIO.LOW)

	while GPIO.input("P8_16") == 0:
		signaloff = time.time()
        while GPIO.input("P8_16") == 1:
   		signalon = time.time()
	timepassed = signalon - signaloff
	distance = timepassed * 17000
	print(distance)
	time.sleep(0.1)
