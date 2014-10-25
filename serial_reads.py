#!usr/bin/python

''' Program to read analog values from arduino.
	Requires another code in arduino.
	Users pyserial module. '''

import serial
import time

values = []
port = serial.Serial('/dev/ttyACM0', 9600, timeout = 2)
count = 0

while count <= 6:
	analog_port = str(count)
	port.write(analog_port)
	print count
	data = port.readline()
	data = data.rstrip()
	print data
	values.insert(count,data)
	count = count + 1
	time.sleep(5)


print values