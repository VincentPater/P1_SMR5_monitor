# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:11:03 2024

@author: Vincent
"""

# Import Modules
import serial_communication as sc
from time import perf_counter



#  Main
def main():
    s = sc.init_serial_communication()
    
    startTime = perf_counter()
    

    while True:    
        char = sc.loopcycle_serial_communication(s)
        print(char)
        if char == '\n':
            print(perf_counter()-startTime)
            pass
        
        





if __name__ == "__main__":
    main()


