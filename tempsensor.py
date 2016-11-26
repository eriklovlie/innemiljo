#!/usr/bin/env python
import smbus
import time

bus = smbus.SMBus(1)

while True:
    data = bus.read_i2c_block_data(0x48, 0)
    msb = data[0]
    lsb = data[1]
    print (((msb << 8) | lsb) >> 4) * 0.0625
    time.sleep(2)
