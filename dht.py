#!/usr/bin/python
#--------------------------------------------
#
#    A script to periodically write a DHTxxxx
#    sensor's data to the disk
#
# Author : Luiz Kill
# Date   : 21/11/2014
#
# http://lzkill.com
#
#--------------------------------------------

import os
import sys
import time
import Adafruit_DHT


PATHNAME = "/var/lib/rpimonitor/stat/dht"
POLLING_DELAY = 5.0


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
				'22': Adafruit_DHT.DHT22,
				'2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
	sensor = sensor_args[sys.argv[1]]
	pin = sys.argv[2]
else:
	print 'usage: sudo ./dht.py [11|22|2302] GPIOpin#'
	print 'example: sudo ./dht.py 2302 4 - Read from an AM2302 connected to GPIO #4'
	sys.exit(1)

try:
	file = open(PATHNAME, "wb")

	humidity = None
	temperature = None

	while True:

		while humidity is None or temperature is None:
			humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		
		file.seek(0)
		file.write('Temp={0:0.1f}*C Hum={1:0.1f}%'.format(temperature, humidity))
		file.truncate()
		
		temperature,humidity = None,None

		time.sleep(POLLING_DELAY)

except Exception as exc:
	print(time.ctime(),exc)
	sys.exit(1)

