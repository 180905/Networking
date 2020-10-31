import socket
S=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg=input()
S.sendto(msg.encode("utf-8"),("127.0.0.1",1234))
data,addr=S.recvfrom(4096)
print("server says")
print(str(data))
S.close()