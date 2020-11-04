#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

#import urllib.request
#import json
import requests
## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    
    ## put fileobject into helmet
    #helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
   # helmetson = json.loads(helmet.decode('utf-8'))
    
    ## display our Pythonic data
   # print("\n\nConverted Python data")
   # print(helmet)
    
   # print('\n\nPeople in Space: ', groundctrl.json['number'])
    #people = helmet ['people']
    #print(people)
    #f = open(groundctrl.json())
    #print(f.read(35))
    #people = groundctrl.json()
    #for x in people:
        #print str(f"{x['name']} is on the {x['craft']}.") 
    print(groundctrl.json(),sep= "-")

main()

