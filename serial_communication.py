# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:59:03 2024

@author: Vincent
"""
import serial
import string


def init_serial_communication(dir_of_serial_port = '/dev/ttyUSB0'):    
    baudrate = 115200
    bytesize = 8
    parity   = 'N'
    stopbits = 1
    stoptime = 1 # seconds
    serialObj   = serial.Serial(dir_of_serial_port, baudrate, bytesize, parity, stopbits, timeout=stoptime)
    
    return serialObj






def loopcycle_serial_communication(serialObj):
    while serialObj.in_waiting > 0:
        output = ""
        output = serialObj.read().decode('ascii')
        print(output, end="")

    
    pass
