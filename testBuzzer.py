import RPi.GPIO as GPIO
from time import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40,GPIO.HIGH)
time.sleep(2)
GPIO.output(40,GPIO.LOW)
#time.sleep(0.1)     
