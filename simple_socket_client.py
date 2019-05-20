
import socket

HOST = '127.0.0.2'  # The server's hostname or IP address
PORT = 6331        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)+1

print('Received', repr(data))