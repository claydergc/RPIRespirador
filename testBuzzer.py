import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38,GPIO.HIGH)
time.sleep(2)
GPIO.output(38,GPIO.LOW)