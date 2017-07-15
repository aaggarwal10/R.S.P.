import webiopi
import RPi.GPIO

GPIO = webiopi.GPIO

def setup():
	
	GPIO.setFunction(7, GPIO.OUT)
	GPIO.setFunction(8, GPIO.OUT)
	GPIO.setFunction(25, GPIO.OUT)
	GPIO.setFunction(11, GPIO.OUT)
	GPIO.setFunction(9, GPIO.OUT)
	GPIO.setFunction(10, GPIO.OUT)
	GPIO.setFunction(23, GPIO.OUT)
	GPIO.setFunction(24, GPIO.OUT)
	GPIO.setFunction(1, GPIO.OUT)
	GPIO.setFunction(18, GPIO.OUT)
	GPIO.setFunction(22, GPIO.OUT)
	GPIO.setFunction(17, GPIO.OUT)
