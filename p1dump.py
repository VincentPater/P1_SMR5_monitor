import serial
import string

output = " "

ser = serial.Serial('/dev/ttyUSB0',115200, 8, 'N', 1, timeout=1)

while True:
	print("---")
	while output != "":
		output = ser.readline().decode('ascii')
		print(output)
