# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP3425
# This code is designed to work with the MCP3425_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=MCP3425_I2CADC#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# MCP3426 address, 0x68(104)
# Send configuration command
#		0x10(16)	Continuous conversion mode, 12-bit Resolution
bus.write_byte(0x68, 0x10)

time.sleep(0.5)

# MCP3425 address, 0x68(104)
# Read data back from 0x00(00), 2 bytes, MSB first
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x68, 0x00, 2)

# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
if raw_adc > 2047 :
	raw_adc -= 4096

# Output data to screen
print "Raw value of the source : %d" %raw_adc
