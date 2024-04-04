import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostbyname(socket.gethostname())
PORT = "Open port"
server.bind((HOST, PORT))
server1 =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server1.bind((HOST, PORT+1))
server.listen(5)
message = ''

while message != '0':
    communication , address = server.accept()
    print(f"Connection Compl..! {address} ")
    while True:
         message = communication.recv(1024).decode('utf-8')
         print(f"We recived : {message}")
         if message == '0':
             communication.close()
             print(f"The connection has close {address}")
         else:
             message = input("Message :")
             communication.send(message.encode('utf-8'))
