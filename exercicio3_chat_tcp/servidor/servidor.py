# cliente.py
# Participantes: Osiel Junior, Fernando Maia, Raul Rodrigues.

import socket
import threading

clientes = []

def encaminhar(origem, mensagem):
    """
    Envia a mensagem recebida de um cliente para o outro.
    """
    for cliente in clientes:
        if cliente != origem:
            try:
                cliente.sendall(mensagem)
            except:
                cliente.close()
                clientes.remove(cliente)

def lidar_com_cliente(cliente, endereco):
    """
    Lida com a comunicação de um cliente específico.
    """
    print(f"[Conectado] Cliente {endereco} conectado.")
    while True:
        try:
            mensagem = cliente.recv(1024)
            if not mensagem:
                break
            if mensagem.decode('utf-8').lower() == 'sair':
                print(f"[Desconectado] Cliente {endereco} saiu.")
                break
            encaminhar(cliente, mensagem)
        except:
            break
    cliente.close()
    clientes.remove(cliente)

def main():
    HOST = '0.0.0.0'  # Escuta em todas as interfaces
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen(2)

        print("[Servidor] Aguardando conexões...")

        while len(clientes) < 2:
            cliente, endereco = servidor.accept()
            clientes.append(cliente)
            thread = threading.Thread(target=lidar_com_cliente, args=(cliente, endereco), daemon=True)
            thread.start()

        print("[Servidor] Dois clientes conectados. Chat iniciado.")

        # Mantém o servidor ativo até os clientes desconectarem
        while clientes:
            pass

        print("[Servidor] Encerrando...")

if __name__ == "__main__":
    main()
