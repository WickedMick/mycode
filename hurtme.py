#!/usr/bin/env python3
print ("Would you like to play a game?")

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
#Define classes
animal = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
veg = ["carrots", "celery"]

#Choose a farm

farm = input("Please choose NE Farm, W Farm, or SE Farm")
if farm == ("NE Farm"): # logic to check if user gave correct answer
    print("Animalistic, are you?")
    choice = 0
if farm == ("W Farm"): # logic to check if user gave correct answer
    print('Keeping it simple, huh?')
    choice = 1
elif farm == ("SE Farm"):    # logic to check choice
    print("Gotta respect the veggies")
    choice = 2
    
else:                 # if answer was wrong
    print("Pick a valid choice!")

#farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         #{"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         #{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
#Define classes
#animal = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
#veg = ["carrots", "celery"]
FORBIDDEN: ["carrots", "celery"]
for animal in farms[choice]["agriculture"]: print(animal)
#create for loop
#for x in farms[0]["agriculture"]:
   # print(x)
#for animal in 

