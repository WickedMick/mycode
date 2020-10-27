#!/usr/bin/env/python3
print 'This quiz will let you know what
 video game you should try, and which you would fail miserably at'

 message = "Judging by your answer..."
 # wrap connection in a float() to accept decimals as numbers
 age = input("What is your age?")

 #if input value was higher or equal to 10
 if age <= 10:
    message = message + 'Too young for video games! Go play OUTSIDE.'
 elif age <= 18:
      message = message + 'Join a sports team!'
 elif connection >= 18:
      message = message + 'Geat a job, ya bum!'
 else:
 message + 'Play by the rules!'
 print(message)
