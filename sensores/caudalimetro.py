import RPi.GPIO as GPIO
from time import time

class Caudalimetro:

    def __init__(self, sensor_pin):
        """docstring for ."""
        self.sensor_pin = sensor_pin
        self.factorConversion = 5.5 #Hz. Para litros por minuto
        self.contadorPulsos = 0
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sensor_pin, GPIO.IN)
        GPIO.add_event_detect(sensor_pin, GPIO.FALLING, callback = self.contadorPulsosCallback)
        self.tiempoAnterior = float(time())

    def contadorPulsosCallback(self,channel):
        self.contadorPulsos += 1

    #debe estar corriendo constantemente
    def getCaudalPorSegundo(self):
        self.caudal = -1.0
        if( float(time()) - float(self.tiempoAnterior) > 1):
            self.tiempoAnterior = time()
            self.caudal = self.contadorPulsos/self.factorConversion
        return self.caudal

    #def getCaudalPorDecimaDeSegundo(self):
    #    self.caudal = -1.0
    #    if( float(time()) - float(self.tiempoAnterior) > 0.1):
    #        self.tiempoAnterior = float(time())
    #        self.caudal = 0.1 * self.contadorPulsos/self.factorConversion
    #    return self.caudal


    def resetContadorPulsos(self):
        self.contadorPulsos = 0
