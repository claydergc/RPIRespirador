from sensores.sensor_presion import SensorPresion
import board

# GPIO setup
sensor_pin = board.D5 #pin 29

sensorPresion = SensorPresion(sensor_pin)

while(True):
        presion = sensorPresion.getPresion()
        print(presion)
