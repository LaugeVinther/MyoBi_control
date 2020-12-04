import busio
import board
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

ads.data_rate = 3300
ads.mode = Mode.CONTINUOUS

# Create single-ended inputs
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
print("ADC-reader blev kørt")
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)


def getData():
        data = []
        
        data.append(chan0.voltage)
        data.append(chan1.voltage)
        data.append(chan2.voltage)
        data.append(chan3.voltage)

        return data
