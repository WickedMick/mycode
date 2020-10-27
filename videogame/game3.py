#!/usr/bin/python3
# running it with ./game3 failed because you didn't have a shebang line

print('This quiz will let you know what video game you should try, and which you would fail miserably at') #added parens

message = "Judging by your answer..."
age = int(input("What is your age?")) 
    # input creates STRINGS... and down below you're comparing "age" to integers.
    # I added the int() function to force the input into becoming an integer

#if input value was higher or equal to 10
if age <= 10:
    message = message + 'Too young for video games! Go play OUTSIDE.'
elif age <= 18:
    message = message + 'Join a sports team!'
elif age >= 18:
    message = message + 'Geat a job, ya bum!'
else:
    message + 'Play by the rules!' # this needed indented correctly

print(message)
