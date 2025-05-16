import socket

HOST = 'localhost'
PORT = 7000  # Porta atualizada para bater com o servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Conectado ao servidor. Digite 'hora' para obter a hora ou 'sair' para encerrar.")

    while True:
        comando = input(">> ").strip()
        s.sendall(comando.encode())

        resposta = s.recv(1024).decode()
        print(resposta.strip())

        if comando.lower() == "sair":
            break

