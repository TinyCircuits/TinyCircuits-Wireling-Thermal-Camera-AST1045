# IR Array Thermal Camera Example
# This example will print out an array of the temperature data read by the camera in Celsius
# Example modified by: Laverena Wienclaw for TinyCircuits

import time
import busio
import board
import adafruit_amg88xx
import tinycircuits_wireling

# Enable and power Wireling Pi Hat
wireling = tinycircuits_wireling.Wireling()
wireling.selectPort(0) # Select port labeled on Pi Hat (0-3)
 
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
 
while True:
    for row in amg.pixels:
        # Pad to 1 decimal place
        print(['{0:.1f}'.format(temp) for temp in row])
        print("")
    print("\n")
    time.sleep(1)
