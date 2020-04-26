import board
import digitalio
import busio
from time import time
import adafruit_bmp280

class SensorPresion:

    def __init__(self, sensor_pin):
        """docstring for ."""
        self.sensor_pin = sensor_pin
        self.spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
        self.bmp_cs = digitalio.DigitalInOut(self.sensor_pin)
        self.bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(self.spi, self.bmp_cs)
        self.bmp280.sea_level_pressure = 1013.25

    #debe estar corriendo constantemente
    def getPresion(self):
        return self.bmp280.pressure
