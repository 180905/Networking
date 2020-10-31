import socket
S=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
S.bind(("127.0.0.1",1234))

while True:
    data,addr=S.recvfrom(4096)
    print(str(data))
    message= input("enter your msg")
    message=bytes(message).encode("utf-8")
    S.sendto(message,addr)