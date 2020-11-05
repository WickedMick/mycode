#!/usr/bin/env python3

import requests ## 3rd party URL lookup
from datetime import datetime
## define the main function
print ("Welcome to the asteroid tracker")
def main():
   # year = int(input('Enter a year'))
   # month = int(input('Enter a month'))
   # day = int(input('Enter a day'))
   # START_DATE = datetime(year, month, day)
    start_date = datetime.strptime(input('Enter Start date in the format y-m-d'), '%Y-%m-%d')
    end_date = datetime.strptime(input('Enter End date in the format y-m-d'), '%Y-%m-%d')
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date'
    #startdate = 'start_date=2018-06-01'  ## start date for data
    ## create a mechanism to utilize enddate
   # year = int(input('Enter a year'))
   # month = int(input('Enter a month'))
   # day = int(input('Enter a day'))
   # END_DATE = datetime(year-month-day)
    enddate = '&end_date'
    
    mykey = '&api_key=Euq74Plrxbzd67HUHhLL3ToJJce9lYyw7t6fwqXc' ## replace this with our API key
    
    neourl = neourl + startdate + enddate + mykey
    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()
