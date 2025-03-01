# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:40:10 2025

@author: Vincent
"""

allCodes = {
      "Version Info" : "1-3:0.2.8",
      "Date-Time" :  "0-0:1.0.0",
      "Equipment ID" :  "0-0:96.1.1",
      "Meter Reading Used Tariff 1" :   "1-0:1.8.1",
      "Meter Reading Used Tariff 2" :  "1-0:1.8.2",
      "Meter Reading Returned Tariff 1" :  "1-0:2.8.1",
      "Meter Reading Returned Tariff 2" :  "1-0:2.8.2",
      "Tariff indicator electricity" : "0-0:96.14.0",
      "Power Used +P" :  "1-0:1.7.0",
      "Power Returned -P" :  "1-0:2.7.0",
      "Number of power failures" :  "0-0:96.7.21",
      "Number of long powe failures" :  "0-0:96.7.9",
      "Power Failure event log" :  "1-0:99.97.0",
      "Number of voltage sags in phase L1" :   "1-0:32.32.0",
      "Number of voltage sags in phase L2" :   "1-0:52.32.0",
      "Number of voltage sags in phase L3" :  "1-0:72.32.0",
      "Number of voltage swells in phase L1" :  "1-0:32.36.0",
      "Number of voltage swells in phase L2" :   "1-0:52.36.0",
      "Number of voltage swells in phase L3" :    "1-0:72.36.0",
      "Text message" :    "0-0:96.13.0",
      "Instantaneous voltage L1" :    "1-0:32.7.0",
      "Instantaneous voltage L2" :   "1-0:52.7.0",
      "Instantaneous voltage L3" :   "1-0:72.7.0",
      "Instantaneous current L1" :   "1-0:31.7.0",
      "Instantaneous current L2" :   "1-0:51.7.0",
      "Instantaneous current L3" :   "1-0:71.7.0",
      "Instantaneous power L1 +P" :   "1-0:21.7.0",
      "Instantaneous power L2 +P" :    "1-0:41.7.0",
      "Instantaneous power L3 +P" :    "1-0:61.7.0",
      "Instantaneous power L1 -P" :    "1-0:22.7.0",
      "Instantaneous power L2 -P" :     "1-0:42.7.0",
      "Instantaneous power L3 -P" :   "1-0:62.7.0",
      "Meter 1 Type" :    "0-1:24.1.0",
      "Meter 1 Indentifier" :  "0-1:96.1.0",
      "Meter 1 Last reading" :   "0-1:24.2.1",
      "Meter 2 Type" :   "0-2:24.1.0",
      "Meter 2 Indentifier" :   "0-2:96.1.0",
      "Meter 2 Last reading" :   "0-2:24.2.1"
    }



class CurrentSmartMeterValues:
    def __init__(self):
        self.date = ''
        self.time = ''
        self.meterUsedT1 = ''
        self.meterUsedT2 = ''
        self.meterReturnedT1 = ''
        self.meterReturnedT2 = ''
        self.tariffIndicator = ''
        self.powerUsed = ''
        self.powerReturned = ''
        self.meterM1reading = ''
        self.meterM2reading = ''
    
    


    def interpretLine (self, textLine):
        
        if len(textLine) == 0:      # Blank textline
            return
        
        
        # Start or end of telegram -> Ignore
        if textLine.find('/') >= 0:     # start of header is a '\', need extra for escape char
            # print('Header')
            return
        if textLine.find('!') >= 0:      # end of telegram starts with '!'
            # print('End of telegram')
            return
        
        
        
        textLineList = textLine.replace('(', ' ').replace(')', ' ').replace('*', ' ').split()
        
        # Update Date and Time
        if textLineList[0] == allCodes["Date-Time"]:
            self.date = '20' + textLineList[1][:2] + '-' + textLineList[1][2:4] + '-' + textLineList[1][4:6]
            
            if textLineList[1][-1] == 'W':
                self.time = textLineList[1][6:8] + ':' + textLineList[1][8:10] + ':' + textLineList[1][10:12] + ' UTC+1'
            elif textLineList[1][-1] == 'S':
                self.time = textLineList[1][6:8] + ':' + textLineList[1][8:10] + ':' + textLineList[1][10:12] + ' UTC+2'
            else:
                self.time = textLineList[1][6:-1] # Should never happen
            return
          
            
          
            
        # Update meterUsedT1
        if textLineList[0] == allCodes["Meter Reading Used Tariff 1"]:
            self.meterUsedT1 = textLineList[1]
            return
        
        # Update meterUsedT2
        if textLineList[0] == allCodes["Meter Reading Used Tariff 2"]:
            self.meterUsedT2 = textLineList[1]     
            return
            
        # Updaye meterReturnedT1
        if textLineList[0] == allCodes["Meter Reading Returned Tariff 1"]:
            self.meterReturnedT1 = textLineList[1] 
            return
        
        # Update meterReturnedT2
        if textLineList[0] == allCodes["Meter Reading Returned Tariff 2"]:
            self.meterReturnedT2 = textLineList[1]
            return
            
        # Update tariffIndicator
        if textLineList[0] == allCodes["Tariff indicator electricity"]:
            self.tariffIndicator = int(textLineList[1])
            return
            
        # Update powerUsed
        if textLineList[0] == allCodes["Power Used +P"]:
            self.powerUsed = textLineList[1] 
            return
        
        # Update powerReturned
        if textLineList[0] == allCodes["Power Returned -P"]:
            self.powerReturned = textLineList[1]    
            return  
        
        # Update meter 1
        if textLineList[0] == allCodes["Meter 1 Last reading"]:
            self.meterM1reading = 'time: '+ textLineList[1] + ' reading: ' + textLineList[2] + ' ' + textLineList[3]      
            return          
        
        # Update meter 2
        if textLineList[0] == allCodes["Meter 2 Last reading"]:
            self.meterM2reading = 'time: '+ textLineList[1] + ' reading: ' + textLineList[2] + ' ' + textLineList[3]     
            return              
        
        return






