from sensores.caudalimetro import Caudalimetro
from time import sleep

# GPIO setup
sensor_pin = 33

caudalimetro = Caudalimetro(sensor_pin)

while(True):
	caudal = caudalimetro.getCaudalPorSegundo()
	if(caudal>=0):
		print(caudal)
		caudalimetro.resetContadorPulsos()
