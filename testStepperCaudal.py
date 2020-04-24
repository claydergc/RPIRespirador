from stepper.stepper import StepperMotor
from time import sleep

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
    deltaTheta = motor.cerrar(0.05625)
    sleep(0.9996875)# = 1-((0.005/32)*2). ((0.005/32)*2) es el tiempo aproximado de la funcion motor.cerrar()

    if( float(time()) - tiempoAnterior > 0.1):        
        caudal = 0.1 * caudalimetro.contadorPulsos/caudalimetro.factorConversion
        caudalimetro.contadorPulsos = 0
        tiempoAnterior = float(time())

    sumTheta += deltaTheta
    f.write("%f %f\n" % (sumTheta,caudal)) #no se considera este tiempo, sin embargo, podría ser importante.

f.close() 
