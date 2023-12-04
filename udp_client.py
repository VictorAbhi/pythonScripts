import socket

target_host = input("Give the url to the target host: \n")
target_port = int(input("Give the target port for udp \n "))

#create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#udp is a connectionless protocol so you need not connect, does'nt have such method
sock.sendto(b"DATA TO SEND",(target_host, target_port))

#receive the data
data, addr = sock.recvfrom(4096)
print(data.decode())
sock.close()