# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:33:04 2024

@author: Vincent
"""

from time import perf_counter


printOn = True

def parser_loop(Buffer):
# Parses Buffer, returns Buffer and textline
   
    
    # find first '\n' in Buffer
    try:
        first_EOL_indx = Buffer.index('\n')
    except:
        #  if no \n found, then no complete line is present -> return None
        return (Buffer, '')
    
        
    
    # if a the first (not necesarily the only) '\n' has been found:
    # place everything up-to and including it into a new variable
    textLine = Buffer[0:first_EOL_indx]
    
    # Keep only the unparsed part of the Buffer
    newBuffer = Buffer[first_EOL_indx+1:]
    
    if printOn:
        print(textLine, end='')
    
    
        
    return (newBuffer, textLine)