#!/usr/bin/env python3
#Networking with python3
import os
#pyexcel is required to run the script
#netmiko is required to run this scriptZZ
from netmiko import ConnectHandler
#pandas must be installed
## USOpen Tournament Switch Checker -- 2018.05.01
''' usopen.py
This script is being designed to provide the following automated tasks:
- ping check the router (import os)
- login check the router (import netmiko)
- determine if interfaces in use are up (import netmiko)
- Apply new configuration (import netmiko) # not yet built

The IPs and device type should be made available via an Excel spreadsheet

'''
import os

## pyexcel and pyexce-xls are required for our program to execute
# python3 -m pip install --user pyexcel
# python3 -m pip install --user pyexcel-xls
import pyexcel

# python3 -m pip install --user netmiko
from netmiko import ConnectHandler

## retrieve data set from excel
def retv_excel(par):
    d = {}
    # create a record object that is an open excel sheet
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        # adds a new IP and driver key:value pair to our dictionary
        d.update( { record['IP'] : record['driver'] } )
    return d # return the completed dictionary

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False


## Check interfaces - Issue "show ip init brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, \
          username=dev_un, password=dev_pw)
        my_command = open_connection.send_command("show ip int brief")       
##retrieve data from spreadsheet
def retv_excel(ppp):
    d = {}
