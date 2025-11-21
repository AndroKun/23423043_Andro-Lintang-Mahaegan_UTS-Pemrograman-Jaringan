import socket
import threading

HOST = '0.0.0.0'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def handle_client(conn, addr):
    print(f"{addr} tersambung")
    clients.append(conn)

    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            broadcast(msg, conn)
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"{addr} terputus")

def broadcast(message, source):
    for client in clients:
        if client != source:
            client.sendall(message)

print("Server chat berjalan...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
