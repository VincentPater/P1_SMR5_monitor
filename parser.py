# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:33:04 2024

@author: Vincent
"""

from time import perf_counter



def parser_loop():
    global GlobalBuffer
    global startTime
    
    
    # find first '\n' in GlobalBuffer
    try:
        first_EOL_indx = GlobalBuffer.index('\n')
    except:
        #  if no \n found, then no complete line is present -> return None
        return None
    
        
    
    # if a the first (not necesarily the only) '\n' has been found:
    # place everything up-to and including it into a new variable
    textLine = GlobalBuffer[0:first_EOL_indx]
    
    # Keep only the unparsed part of the GlobalBuffer
    GlobalBuffer = GlobalBuffer[first_EOL_indx+1:]
    
    print(textLine)
    print(str(perf_counter()-startTime))
    
    
    
    return None