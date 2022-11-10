import socket

message = "Helloooo"
host = socket.gethostname()

client_socket = socket.socket()
client_socket.connect((host, 10000))
client_socket.send(message.encode())
print(client_socket.recv(1024).decode())
client_socket.close()

