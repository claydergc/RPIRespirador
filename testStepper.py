from stepper.stepper import StepperMotor
from time import sleep

# GPIO setup
enable_pin = 12
#step_pin = 23
#dir_pin = 24
mode_pins = (13, 15, 18)

# Stepper motor setup
step_type = '1/32'
fullstep_delay = .005

# create object
motor = StepperMotor(enable_pin, step_pin, dir_pin, mode_pins, step_type, fullstep_delay)

theta = 1.8 #angulo a mover en el motor
f= open("data.txt","wr+")


#motor.enable(True)        # enables stepper driver
#motor.run(6400, True)     # run motor 6400 steps clowckwise
#sleep(0.5)
#motor.run(6400, False)    # run motor 6400 steps counterclockwise
#motor.enable(False)       # disable stepper driver

motor.girar(theta)
f.write("%d\n" % theta) #se guarda el angulo en el arhivo data.txt

f.close() 
