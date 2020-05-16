import socket
import threading

'''
1. Define PORT for communication
2. Define SERVER with IP Address of host machine
3. Define the default address structure
4. Define the address family (IPv4 for AF_INET here) and connection protocol (TCP for Sock_Stream)
5. Define handle_client function that will be used for threads.
'''

HEADER = 64
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print (f"[{addr}] {msg}")
    conn.close()

def start():
    print ("[STARTING] Server is starting...")
    server.listen()
    print (f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print (f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

start()