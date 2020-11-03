#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os
import time

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

#def main()
## how to connect (see other labs on using id_rsa private/public keypairs)
while True:
    username == input("Username:")
    password == input("Password:")
    if username == 'bender' and password == 'alta3':
            time.sleep(1)
            print ("Login successful!")
            logged()

    else:
        print ("Password did not match!")

#def logged()
   # print ("Welcome to my nightmare")

#main()

t.connect(username= ("bender"), password= ("alta3")
        #  Make an sftp connection object

sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

