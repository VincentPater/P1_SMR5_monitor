# Update
Project halted in favor of ESP32 -> MQTT -> (e.g. HomeAssistent) solution.
I'll leave this public in case anybody wants to continue.


# P1_SMR5_monitor

Done:

1. Read char by char, put in buffer
2. Separate buffer into individual lines
3. Make conf file for user settings
4. Find and read from list that contains all the p1 codes
5. Translate string-data into data container object

Todo:

6. CRC implementation (similar to https://gathering.tweakers.net/forum/list_messages/2250716)
7. Show data via local web page
8. Archival of data every day

Future Features:
- Log energy use and production per day/week/month?
- Branch this repository into one where power is distributed and optimised over several consumers e.g. electric boiler
