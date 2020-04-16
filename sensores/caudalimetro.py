import RPi.GPIO as GPIO
from time import time

class Caudilimetro:

    contadorPulsos = 0
    factorConversion = 5.5

    def __init__(self, sensor_pin):
        """docstring for ."""
        self.sensor_pin = sensor_pin
        GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor_pin, GPIO.IN)
	GPIO.add_event_detect(sensor_pin, GPIO.RISING, callback = contadorPulsos)
	tiempoAnterior = time.time()

    def contadorPulsos(self,channel):
	global contadorPulsos
	start = time.time()
	contadorPulsos += 1
	    
    #debe estar corriendo constantemente
    def getCaudal(self):	
	start = time.time()
	caudal = -1
	if( time.time() - tiempoAnterior > 1):
	    tiempoAnterior = time.time()
	    caudal = contadorPulsos/factorConversion
	return caudal
