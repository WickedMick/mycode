#!/usr/bin/env python3
ipchk = "192.168.0.1"

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)

else:    # if data is NOT provided
   print("You did not provide input.") # indented under else
