import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(3)  # timeout saat connect

try:
    client.connect((HOST, PORT))
except socket.timeout:
    print("Koneksi timeout!")
    exit()

client.settimeout(2)  # timeout saat membaca

try:
    data = client.recv(1024).decode()
    print("Dari server:", data)
except socket.timeout:
    print("Koneksi timeout!")
