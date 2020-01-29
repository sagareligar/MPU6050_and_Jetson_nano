//hey 

import serial
with serial.Serial('/dev/ttyACM1',115200) as ser:  # '/dev/ttyACM1' is serial port name
  while True:
  	print(ser.readline())
#testa
