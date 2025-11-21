import socket

HOST = '0.0.0.0'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server berjalan di port {PORT}")

while True:
    conn, addr = server.accept()
    print(f"Terhubung dengan {addr}")

    data = conn.recv(1024).decode()
    print("Dari client:", data)

    conn.sendall(data.encode())  # echo balik

    conn.close()
