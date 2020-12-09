#!/usr/bin/env python3

# message = 'The movie is about to begin, we recommend' 
message = 'The speed of your network and performance '
# wrap connection in a float() to accept decimals as numbers
# connection = float(input("What is your connection speed in Mbps?"))
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

# if input value was higher or equal to 25
# if connection >= 25:
#    message = message + 'setting video to 4k.'
# elif connection >= 5:
#    message = message + 'setting video to 1080p.'
# elif connection >= 2:
#    message = message + 'setting video to 720p.'
# else:
#    message = message + 'finding another access network.'
#print(message)


