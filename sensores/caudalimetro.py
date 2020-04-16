import RPi.GPIO as GPIO
from time import time

class Caudalimetro:

    def __init__(self, sensor_pin):
        """docstring for ."""
        self.sensor_pin = sensor_pin
	self.factorConversion = 5.5
	self.contadorPulsos = 0
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sensor_pin, GPIO.IN)
	GPIO.add_event_detect(sensor_pin, GPIO.FALLING, callback = self.contadorPulsosCallback)
	self.tiempoAnterior = time()

    def contadorPulsosCallback(self,channel):
	self.contadorPulsos += 1

    #debe estar corriendo constantemente
    def getCaudal(self):

	self.caudal = -1.0
	if( time() - self.tiempoAnterior > 1):
	    self.tiempoAnterior = time()
	    self.caudal = self.contadorPulsos/self.factorConversion
	return self.caudal

    def resetContadorPulsos(self):
	self.contadorPulsos = 0
