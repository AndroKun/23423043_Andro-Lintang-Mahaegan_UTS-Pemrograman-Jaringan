import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def terima():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            break

threading.Thread(target=terima).start()

while True:
    pesan = input("")
    client.sendall(pesan.encode())
