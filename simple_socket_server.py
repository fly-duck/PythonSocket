import socket 

import sys 
HOST = '127.0.0.2'  # Standard loopback interface address (localhost)
PORT = 6331        # Port to listen on (non-privileged ports are > 1023)



# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # Bind the socket to the port
# server_address = ('localhost', 233)
# print (sys.stderr, 'starting up on %s port %s' % server_address)

# host = socket.gethostname()
# print(host)
# sock.bind(server_address)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("sb")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)