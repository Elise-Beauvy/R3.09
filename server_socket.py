import socket

reply = "reçu"
host = socket.gethostname()

server_socket = socket.socket()
server_socket.bind((host, 10000))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
print(data)
conn.send(reply.encode())
conn.close()