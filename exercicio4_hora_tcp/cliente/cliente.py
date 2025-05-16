import socket

HOST = 'localhost'
PORT = 7000  # Porta atualizada para bater com o servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Recebe a hora uma vez
    data = s.recv(1024)
    print("Hora recebida do servidor:", data.decode())

