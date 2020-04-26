import RPi.GPIO as GPIO
from stepper.stepper import StepperMotor
from time import sleep
from time import time

# GPIO setup
step_pin1 = 24
dir_pin1 = 22
mode_pins1 = (36, 32, 26)

step_pin2 = 40
dir_pin2 = 38
mode_pins2 = (11, 13, 15)


# Stepper motor setup
step_type = '1/32'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# create object
motor1 = StepperMotor(step_pin1, dir_pin1, mode_pins1, step_type)
motor2 = StepperMotor(step_pin2, dir_pin2, mode_pins2, step_type)

sumTheta = 0.0

while sumTheta < 90.0:
    deltaTheta1 = motor1.abrir(0.45)
    sleep(0.01)
    deltaTheta1 = motor2.abrir(0.45)
    sleep(0.01)
    sumTheta += 0.45
