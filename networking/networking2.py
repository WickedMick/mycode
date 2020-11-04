#!/usr/bin/env python3

from netmiko import ConnectHandler
import os

print("Before config push")

device = ConnectHandler(device_type='*’, ip='*′, username=’*’, password=’*’)
output = device.send_command(“show running-config interface fastEthernet 0/0”)
print (output)

configcmds=[“interface fastEthernet 0/0”, “description my test”] device.send_config_set(configcmds)

print (“After config push”)
output = device.send_command(“show running-config interface fastEthernet 0/0”)
print (output)

device.disconnect()
