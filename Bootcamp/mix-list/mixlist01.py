#!/usr/bin/env python3

# create list containing items
# my_list = [ "192.168.0.5", 5060, "UP" ]

# display first item and so forth
# print("The first itme in the list (IP): " + my_list[0] )

# print("The second item in the list (port): " + str(my_list[1]) )

# print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# print("When I " + new_list[5] + "into IP address " + new_list[4] + "or " + new_list[3] + "I am unable to.")


# IMPORTANT = f.string approach/method
easier = print(f"When I {new_list[5]} into IP address {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")

print(easier)

