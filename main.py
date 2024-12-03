# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:11:03 2024

@author: Vincent
"""

# Import Modules
import serial_communication as sc




#  Main
def main():
    s = sc.init_serial_communication()

    while True:    
        sc.loopcycle_serial_communication(s)
















if __name__ == "__main__":
    main()
