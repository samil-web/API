import socket
HOST = 'localhost'
PORT = 1024

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
while (1):
    conn, addr = socket.accept()
    reqFile = conn.recv(1024)
    with open(reqFile, 'rb') as file_to_send:
        for data in file_to_send:
            conn.sendall(data)
    conn.close()

socket.close()