import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostbyname(socket.gethostname())
PORT = 456
server.bind((HOST, PORT))
server.listen(5)
message = ''

while message != '0':
    try:
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
    except Exception as e:
        print(e)


server.close()
