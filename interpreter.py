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
        
        # Start or end of telegram -> Ignore
        if textLine[0] == '\\':     # start of header is a '\', need extra for escape char
            print('Header')
            return
        if textLine[0] == '!':      # end of telegram starts with '!'
            print('End of telegram')
            return
        
        # Update Date and Time
        if textLine.find(allCodes["Date-Time"]) >= 0:
            indx = len(allCodes["Date-Time"])+1
            self.date = '20' + textLine[indx:indx+2] + '-' + textLine[indx+2:indx+4] + '-' + textLine[indx+4:indx+6]
            
            if textLine[-2] == 'W':
                self.time = textLine[indx+6:indx+8] + ':' + textLine[indx+8:indx+10] + ':' + textLine[indx+10:indx+12] + ' UTC+1'
            elif textLine[-2] == 'S':
                self.time = textLine[indx+6:indx+8] + ':' + textLine[indx+8:indx+10] + ':' + textLine[indx+10:indx+12] + ' UTC+2'
            else:
                self.time = textLine[indx+6:-1]
            return
          
            
          
            
        # Update meterUsedT1
        if textLine.find(allCodes["Meter Reading Used Tariff 1"]) >= 0:
            indx = len(allCodes["Meter Reading Used Tariff 1"])+1
            self.meterUsedT1 = textLine[indx:-1]
            return
        
        # Update meterUsedT2
        if textLine.find(allCodes["Meter Reading Used Tariff 2"]) >= 0:
            indx = len(allCodes["Meter Reading Used Tariff 2"])+1
            self.meterUsedT2 = textLine[indx:-1]      
            return
            
        # Updaye meterReturnedT1
        if textLine.find(allCodes["Meter Reading Returned Tariff 1"]) >= 0:
            indx = len(allCodes["Meter Reading Returned Tariff 1"])+1
            self.meterReturnedT1 = textLine[indx:-1] 
            return
        
        # Update meterReturnedT2
        if textLine.find(allCodes["Meter Reading Returned Tariff 2"]) >= 0:
            indx = len(allCodes["Meter Reading Returned Tariff 2"])+1
            self.meterReturnedT2 = textLine[indx:-1]
            return
            
        # Update tariffIndicator
        if textLine.find(allCodes["Tariff indicator electricity"]) >= 0:
            indx = len(allCodes["Tariff indicator electricity"])+1
            self.tariffIndicator = int(textLine[indx:-1])
            return
            
        # Update powerUsed
        if textLine.find(allCodes["Power Used +P"]) >= 0:
            indx = len(allCodes["Power Used +P"])+1
            self.powerUsed = textLine[indx:-1]     
            return
        
        # Update powerReturned
        if textLine.find(allCodes["Power Returned -P"]) >= 0:
            indx = len(allCodes["Power Returned -P"])+1
            self.powerReturned = textLine[indx:-1]     
            return  
        
        # Update meter 1 (Gas probably)
        if textLine.find(allCodes["Meter 1 Last reading"]) >= 0:
            indx = len(allCodes["Meter 1 Last reading"])+1
            self.meterM1reading = textLine[indx:-1]     
            return          
        
        # Update meter 2 (Water probably)
        if textLine.find(allCodes["Meter 2 Last reading"]) >= 0:
            indx = len(allCodes["Meter 2 Last reading"])+1
            self.meterM2reading = textLine[indx:-1]     
            return              
        
        return






