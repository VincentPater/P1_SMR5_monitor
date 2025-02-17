# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:11:03 2024

@author: Vincent
"""

# Import Modules
import configparser
import serial_communication as sc
import parser as psr

from time import perf_counter


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
    

    # Loop infinitely until keyboard interrupt
    while True:
        # Read from Serial port into Buffer
        Buffer += sc.loopcycle_serial_communication(s)
        
        # Buffer contains no, partial or even multiple text lines -> parse them
        Buffer, textLine = psr.parser_loop(Buffer, printOn)
        
        # Extract info from textlines
 
        
        












# %%                --- Setup so program runs ---


if __name__ == "__main__":
    main()


