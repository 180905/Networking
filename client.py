import socket
s=socket.socket()
host="192.168.156.1"
port= 999

s.connect((host, port))

while True:
    data = str( s.recv(1024))
    print("server: " + data)
    resp=str(input("client: "))
    s.send(resp )