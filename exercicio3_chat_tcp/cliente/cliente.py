# cliente.py
# Participantes: Osiel Junior, Fernando Maia, Raul Rodrigues.

import socket
import threading

def receber_mensagens(sock):
    """
    Thread para receber mensagens do servidor e exibi-las na tela.
    """
    while True:
        try:
            mensagem = sock.recv(1024).decode('utf-8')
            if not mensagem:
                break
            print(f"\n[Recebido] {mensagem}")
        except:
            print("Erro ao receber mensagem. Encerrando conexão.")
            break

def main():
    HOST = '127.0.0.1'  # Endereço do servidor
    PORT = 12345        # Porta do servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        try:
            cliente.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Servidor indisponível.")
            return

        print("Conectado ao chat! Digite 'sair' para encerrar.\n")

        # Inicia thread para receber mensagens
        thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,), daemon=True)
        thread_receber.start()

        # Loop principal para enviar mensagens
        while True:
            msg = input()
            if msg.lower() == 'sair':
                cliente.sendall("sair".encode('utf-8'))
                break
            cliente.sendall(msg.encode('utf-8'))

        print("Você saiu do chat.")

if __name__ == "__main__":
    main()