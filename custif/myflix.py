#!/usr/bin/env python3

message = 'The speed of your network and performance '
connection = float(input("What is your speed/performance"))
if connection >= 200:
    message = message + 'is amazing.'
elif connection >= 100: 
    message = message + 'is great.'
elif connection >= 50:
    message = message + 'is ok.'
elif connection >= 25:
    message = message + 'is bad.'
else: 
    message = message + 'is non-existant.'
print(message)


