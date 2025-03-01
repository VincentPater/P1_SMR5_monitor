# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:11:03 2024

@author: Vincent
"""

# Import Modules
import configparser
import serial_communication as sc
import parser as psr
from interpreter import CurrentSmartMeterValues

from time import time


#%%                 --- Main ---
def main():
    # Read configuration file
    conf_obj = configparser.ConfigParser()
    with open("settings.ini","r") as file_object:
        conf_obj.read_file(file_object)
        try:
            ttydir = conf_obj.get("USER SETTINGS","dir_of_serial_port")                     # Case sensitive!
            printOn = conf_obj.get("USER SETTINGS","print_to_console").upper() == 'TRUE'    # Case insensitive
        except:
            raise Exception("Settings.ini is incorrect. Perhaps you made a typo")
    
    # Initialisation
    s = sc.init_serial_communication(ttydir)
    Buffer = ""
    currentMeterValues = CurrentSmartMeterValues()
    oldTime = time()
    

    # Loop infinitely until keyboard interrupt
    while True:
        # Read from Serial port into Buffer
        Buffer += sc.loopcycle_serial_communication(s)
        
        # Buffer contains no, partial or even multiple text lines -> parse them
        Buffer, textLine = psr.parser_loop(Buffer, printOn)
        
        # Extract info from textlines
        currentMeterValues.interpretLine(textLine)
        
        # Temp: print values in obj
        curTime = time()
        if (curTime - oldTime) >= 2:
            print('----------')
            print(currentMeterValues.date)
            print(currentMeterValues.time)
            print(currentMeterValues.meterUsedT1)
            print(currentMeterValues.meterUsedT2)
            print(currentMeterValues.meterReturnedT1)
            print(currentMeterValues.meterReturnedT2)
            print(currentMeterValues.tariffIndicator)
            print(currentMeterValues.powerUsed)
            print(currentMeterValues.powerReturned)
            print(currentMeterValues.meterM1reading)
            print(currentMeterValues.meterM2reading)
            print('----------')
            print('')
            oldTime = curTime
        












# %%                --- Setup so program runs ---


if __name__ == "__main__":
    main()


