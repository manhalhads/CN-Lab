# -*- coding: utf-8 -*-
"""Serverq1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iWaltptjfLWmtxBqDjH1SBs8n-B4mzxt
"""

import socket
import sys

idlist = []
def check_id( a):
 if a in idlist:
    return 1
 else:
    return 0
# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to server address and port 81
server_address = ('localhost', 81)
tcp_socket.bind(server_address)


# Listen on port 81
tcp_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()

    try:
        print("Connected to client IP: " + client[0])
        while True:
            # Receive and print data 32 bytes at a time, as long as the client is sending something
            data = connection.recv(32)
            if data:
                stringdata = data.decode('utf-8')
                print("Received data: "+ data.decode())
                if check_id(stringdata[31]) == 0:
                    message = 'Hello I am server. Your received id is ' + stringdata[31]
                    idlist.append(stringdata[31])
                else:
                    message = 'Hello I am server. Client id ' + stringdata[31] + ' is already here.'
                connection.sendall(message.encode())
            else:
                print('No more data from client')
                break

    finally:
       connection.close()
