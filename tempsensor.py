#!/usr/bin/env python
import smbus
import time
import subprocess
import sys

api_key = sys.argv[1]
bus = smbus.SMBus(1)

while True:
    data = bus.read_i2c_block_data(0x48, 0)
    msb = data[0]
    lsb = data[1]
    ftemp = (((msb << 8) | lsb) >> 4) * 0.0625
    stemp = "{:.1f}".format(ftemp)
    print stemp
    proc = subprocess.Popen([
        "curl",
        "--fail",
        "--header", "X-THINGSPEAKAPIKEY: {}".format(api_key),
        "-XPOST",
        "https://api.thingspeak.com/update?field1={}".format(stemp),
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if proc.returncode != 0:
        print out
        print err
        exit(1)
    time.sleep(60)
