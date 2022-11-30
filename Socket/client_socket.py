import socket
import time
import multiprocessing
import threading

msgcl = ""
msgsrv = ""

host = socket.gethostname()

def client():

    client_socket = socket.socket()
    client_socket.connect((host, 10009))

    msgsrv = ""
    while msgsrv != "bye" and msgsrv != "arret":
        msgsrv = client_socket.recv(1024).decode()
        print(msgsrv)
    client_socket.close()

if __name__ == '__main__':
    client_socket = socket.socket()
    start = time.perf_counter()
    p1 = threading.Thread(target=client(), args=[client_socket])
    p1.start()

    while msgcl != "bye" and msgcl != "arret":
        msgcl = input("Amon:")
        client_socket.send(msgcl.encode())

    p1.join()
    client_socket.close()