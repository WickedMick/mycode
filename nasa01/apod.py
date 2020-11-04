#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser
#take user input
print("Would you like to select custom parameters? 1 for Yes or 2 for No")
x = int(input())
if x < 2:
    print  ("\n1. Date"
            "\n2. hd"
            "\n3. api_key")
else:pass
x= int(input())
if x = 1:
    print(
#define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=Euq74Plrxbzd67HUHhLL3ToJJce9lYyw7t6fwqXc' ## this is our api key

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

