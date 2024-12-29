# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:59:03 2024

@author: Vincent
"""
import serial
import string
from time import perf_counter




def init_serial_communication(dir_of_serial_port = '/dev/ttyUSB0'):    
    baudrate = 115200
    bytesize = 8
    parity   = 'N'
    stopbits = 1
    stoptime = 1 # seconds
    serialObj   = serial.Serial(dir_of_serial_port, baudrate, bytesize, parity, stopbits, timeout=stoptime)

    
    return serialObj






def loopcycle_serial_communication(serialObj):
    global GlobalBuffer
    
    """
    It has been found that often more than 1 char is placed into the serial buffer
    yet not necessarily the entire line. 40 - 60 but also 5 have been observed
    Sometimes also MORE than one message is included
    """
    
    # Read one or more characters until serial buffer is empty
    while serialObj.in_waiting > 0:
        # print(serialObj.in_waiting)
        GlobalBuffer += serialObj.read().decode('ascii')
        pass
    
    return None
    

