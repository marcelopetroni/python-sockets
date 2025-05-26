import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
print("Conectado ao servidor!")

while True:
    msg = input("Cliente: ")
    if msg == "sair":
        break
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024)
    print("Servidor:", data.decode())

client_socket.close()
