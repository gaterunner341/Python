"""
The purpose of this code is to obtain a user's input and send a GET request
to the website provided.
Author: Phillip Kittelson
Date: 27 July 2019
"""

import socket
import sys

print("Socket Connection Program v1.1")
print("This program attemps to send a GET request to a requested website")
print()
userinput = input("What website would you like to send a GET request to: ")
print()

# Creates instance of socket using internet and TCP protocols
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created...")
except  socket.error:
    print("Failed to create socket")
    sys.exit()

try:
    host = socket.gethostbyname(userinput) # cretes host
    print("Host created...")
except socket.gaierror:
    print("Failed to get host")
    sys.exit()


mysock.connect((host,80)) # Create connection, double () means tuple

message = "GET / HTTP/1.1\r\n\r\n" # Craft HTTP GET message to send
print("Message crafted...")

print("Encoding message in UTF-8...") # Encode str message to bits
try:
    emessage = message.encode('utf-8')
    print("Message encoding success")
except:
    print("Message encoding failed")

try:
    mysock.sendall(emessage) # Send message
    print("Encoded message sent...")
except socket.error:
    print("Failed to send")
    sys.exit()

data= mysock.recv(1000) # Receive response
print("Response received...")
print()

print("Printing out received response...") # Print out received data
print()
print(data)

mysock.close() # Close socket
