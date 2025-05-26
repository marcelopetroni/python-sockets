import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Servidor escutando em localhost:12345")
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Cliente:", data.decode())
    resposta = input("Servidor: ")
    conn.sendall(resposta.encode())

conn.close()
