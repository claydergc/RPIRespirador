import RPi.GPIO as GPIO
from time import sleep

class StepperMotor:
    def __init__(self, step_pin, dir_pin, mode_pins, step_type):
        """docstring for ."""
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.step_type = step_type
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(mode_pins, GPIO.OUT)
        self.resolution = {'Full':(0, 0, 0),
                    'Half':(1, 0, 0),
                    '1/4':(0, 1, 0),
                    '1/8':(1, 1, 0),
                    '1/16':(0, 0, 1),
                    '1/32':(1, 0, 1)}
        self.microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
        self.delay = .005/self.microsteps[step_type]
        GPIO.output(mode_pins, self.resolution[step_type])

    def run(self, steps, clockwise):
        GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(self.delay)

    def direccionRotacion(self, theta):
        if theta > 0:
           return 1
        else:
           return 0

    #1 micropaso 1/32 = 0.05625 grados. 1.8/32
    def girar(self, theta): #resolucion del motor
	#GPIO.output(self.dir_pin, self.direccionRotacion(theta))
        #pasos = round(theta/0.05625, 0)
        pasos = round(theta/(1.8/self.microsteps[self.step_type]), 0)
        self.run(int(pasos),self.direccionRotacion(theta))
        #return pasos*0.05625
        return pasos*(1.8/self.microsteps[self.step_type])

    def cerrar(self, theta): #resolucion del motor
        pasos = round(theta/(1.8/self.microsteps[self.step_type]), 0)
        self.run(int(pasos),1) #cerrar=1 con engranes. con faja el 1 seria 0
        #return pasos*0.05625
        return pasos*(1.8/self.microsteps[self.step_type])

    def abrir(self, theta): #resolucion del motor
        pasos = round(theta/(1.8/self.microsteps[self.step_type]), 0)
        self.run(int(pasos),0) #abrir=0 con engranes. con faja el 0 seria 1
        #return pasos*0.05625
        return pasos*(1.8/self.microsteps[self.step_type])
