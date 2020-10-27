#!/usr/bin/python3
# running it with ./game3 failed because you didn't have a shebang line
print ("Hello there! What is your name? I will help you make your life better.")

print ('This quiz will let you know what video game you should try, and which you would fail miserably at') #added parens
 
message = "Judging by your answer..."
age = int(input("What is your age?")) 
     # input creates STRINGS... and down below you're comparing "age" to integers.
     # I added the int() function to force the input into becoming an integer
 
 #if input value was higher or equal to 10
if age <= 10:
     message = message + "Too young for video games! Go play OUTSIDE."
 
elif age <= 18:
     message = message + "Join a sports team!"
elif age >= 18:
    message = message + "Get a job, ya bum!"
else:
    message + "Play by the rules!" # this needed indented correctly
 
print(message)

print("Kidding. Let us see what is out there for you")

message = "Ok..."

interests = str(input("What is your quest...or interests?"))

if interests == 'football':
    message == message + "Try Madden"
elif interests == "fishing":
    message = message + "Try Bass Pro"
elif interests == "shooting":
    message = message + "Try Halo"
elif interests == "baseball":
    message = message + "Try MLB2K"
elif interests == "basketball":
    message = message + "Try NBA2K"
elif interests == "crime":
    message = message + "Try Arkham Knight"

else:
    message = message + "Maybe stick with MarioKart"

print(message)

print ("Now get out there and make a difference, you window licker!")
