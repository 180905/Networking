import socket
import sys
import datetime

# create socket(connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        
        host=""
        port=999
        s=socket.socket() #create socket function
    
    except socket.error as msg:
        print("socket creation error: " + str(msg))

# Binding socket with host and port and listining for connection
def bind_socket():
    try:
        global host
        global port
        global s
        print("binding the port " + str(port))

        s.bind((host,port))
        s.listen(4)

    except socket.error as msg:
        print("socket binding error" + str(msg)+"Retrying...")
        bind_socket()

# Establishing connection with a clint(socket must be listining)
def socket_accept():
    conn,adress = s.accept()#it gives two output one for adress and one
    print("connection has been established "+ " ip "+ adress[0] +str(adress[1]) )
    send_command(conn)#after connection send data or command
    conn.close()

# send command to client 
def send_command(conn):
    while True:
        cmd=input("server: ")
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024))
            print("client: " + client_response)
            # conn.send(cmd)


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()