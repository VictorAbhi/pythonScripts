import socket
import threading

def main():
    ip_addr = '127.0.0.1'
    port = 9998
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip_addr,port))
    
    server.listen(5)
    print(f'[*]Listening on{ip_addr}:{port}')
    
    while True:
        client, address = server.accept()
        print(f'[*]Received requests from {address[0]}:{address[1]},')
        
        client_handler = threading.Thread(target=client_handle, args=(client,))
        client_handler.start()


def client_handle(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACKnowledged by the server')
        


if __name__=='__main__':
    main()