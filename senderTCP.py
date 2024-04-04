import socket
import time
HOST = '192.168.1.142'
PORT = 456

sent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sent.connect((HOST, PORT))

i = 1
while i != 0:
    message = input("Message to Server :")
    sent.send(message.encode('utf-8'))
    print(sent.recv(1024).decode('utf-8'))
    i = int(input("What do you want to continue? (0=NO,1=YES)"))

