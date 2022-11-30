import socket
import time
import multiprocessing
import threading

msgsrv = ""
msgcl = ""

host = socket.gethostname()
def serveur():

    while msgcl != "bye" and  msgcl != "arret":
            msgcl = conn.recv(1024).decode()
            print(msgcl)

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind((host, 10009))
    server_socket.listen(1)
    conn, address = server_socket.accept()

    start = time.perf_counter()
    p1 = threading.Thread(target=serveur, args=[conn])
    p1.start()

    while msgsrv != "bye" and msgsrv != "arret":
        msgsrv = str(input("Isis:"))
        conn.send(msgsrv.encode())

    p1.join()
    server_socket.close()