import socket

SERVER_IP = '127.0.0.1'  # Replace with the actual server IP address
SERVER_PORT = 9998  # Replace with the actual server port

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    message = "Hello, server!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024)
    print(f"Received response: {response.decode('utf-8')}")

    client_socket.close()

if __name__ == '__main__':
    main()

