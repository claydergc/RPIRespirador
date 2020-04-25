from stepper.stepper import StepperMotor
from sensores.caudalimetro import Caudalimetro
from time import sleep
from time import time

# GPIO setup
step_pin = 24
dir_pin = 22
mode_pins = (36, 32, 26)

# Stepper motor setup
step_type = '1/32'
caudal_pin = 11

# create object
motor = StepperMotor(step_pin, dir_pin, mode_pins, step_type)
f= open("./dataMotorCaudal.txt","w+") #abrir archivo para lectura y escritura
caudalimetro = Caudalimetro(caudal_pin)

tiempoAnterior = float(time())

sumTheta = 0.0
while sumTheta < 1619.0:
    t0 = time()
    #deltaTheta = motor.cerrar(0.05625) #quizas paso muy pequeño
    deltaTheta = motor.cerrar(1.8)
    #sleep(0.25) #verificar cuanto delay necesito para generar un minimo de pulsaciones por unidad de tiempo
    t1 = time()
    caudal = (t1-t0) * caudalimetro.contadorPulsos/caudalimetro.factorConversion
    sumTheta += deltaTheta
    f.write("%f %f\n" % (sumTheta,caudal)) #no se considera este tiempo, sin embargo, podría ser importante.
    caudalimetro.contadorPulsos = 0

f.close() 
