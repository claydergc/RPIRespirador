import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class ECG:

    def __init__(self):
        """docstring for ."""
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.chan = AnalogIn(self.ads, ADS.P0)

    #debe estar corriendo constantemente
    def getVoltage(self):
        return self.chan.voltage

    def getRawValue(self):
        return self.chan.value
