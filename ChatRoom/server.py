import socket
import select
import sys
import threading
import _thread


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def clientthread(conn, addr):
    conn.send("Welcome TO chatROOM !!")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print(f'< {addr[0]} > {message}')
                
                message_to_send = f'< {addr[0]} > {message}'
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("[-] ERROR !! \n Correct Usage : \n script IPAddress Port")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server.bind((IP_address, Port))

#listens for atmost 100 connections
server.listen(100)

list_of_clients = []

while True:

    conn, addr = server.accept()

    list_of_clients.append(conn)

    print(addr[0] + " connected")

    _thread.start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
