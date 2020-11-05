#!/usr/bin/env python3
import json
#import time
file= open("mommas.json", "r").read()

mommas= json.loads(file)
#x= (east_coast_mamas)
#East Coast Mommas Names
for x in mommas["east_coast_mommas"]:
    print(x["name"])

   # time.sleep(3)
#All Mommas Names
for x in mommas.keys():
#for x in mommas[0]:
    for y in mommas[x]:  
        print(y["name"])
#Momma Jokes
momma_names= []

for x in mommas.keys():
    for y in mommas[x]:
        momma_names.append(y["name"])

print(f"Yo momma {random.choice(momma_names)} is {random.choice})

