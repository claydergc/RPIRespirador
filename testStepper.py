from stepper.stepper import StepperMotor
from time import sleep

# GPIO setup
step_pin = 24
dir_pin = 22
mode_pins = (36, 32, 26)

# Stepper motor setup
#step_type = '1/32'
step_type = 'Full'

# create object
motor = StepperMotor(step_pin, dir_pin, mode_pins, step_type)

theta0 = 90 #angulo a mover en el motor
f= open("./angles_data.txt","r+") #abrir archivo para lectura y escritura


#motor.enable(True)        # enables stepper driver
#motor.run(6400, True)     # run motor 6400 steps clowckwise
#sleep(0.5)
#motor.run(6400, False)    # run motor 6400 steps counterclockwise
#motor.enable(False)       # disable stepper driver

theta1 = motor.girar(theta0) # angulo al que se llega si el numero de pasos calculados no es entero
sleep(0.5)
#f.write("%f\n" % theta1) #se guarda el angulo en el arhivo data.txt
f.write("%f" % theta1) #se guarda el angulo en el arhivo data.txt
f.close() 
