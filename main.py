# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:11:03 2024

@author: Vincent
"""

# Import Modules
import serial_communication as sc
import parser as psr

from time import perf_counter


#%%                 --- Main ---
def main():
    # Initialisation
    s = sc.init_serial_communication()
    
    GlobalBuffer = ""
    


    # Loop infinitely until keyboard interrupt
    while True:    
        sc.loopcycle_serial_communication(s)
        
        startTime = perf_counter()
        psr.parser_loop()
        
        












# %%                --- Setup so program runs ---


if __name__ == "__main__":
    main()


