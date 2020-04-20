from sensores.sensor_presion import SensorPresion
import board

# GPIO setup
sensor_pin = board.D12

sensorPresion = sensorPresion(sensor_pin)

while(True):
	presion = sensorPresion.getPresion()
	print(presion)
