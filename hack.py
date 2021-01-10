import socket
import sys


args = sys.argv
ip = str(args[1])
port = int(args[2])
message = str(args[3])
buffer_size = 1024

my_socket = socket.socket()
address = (ip, port)
my_socket.connect(address)
message = message.encode()
my_socket.send(message)
response = my_socket.recv(buffer_size)
print(response.decode())
my_socket.close()
