# servidor.py
# Participantes: Osiel Junior, Fernando Maia, Raul Rodrigues.

import socket

def main():
    host = '0.0.0.0'
    port = 6000

    # Cria o socket UDP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((host, port))

    print(f"[+] Servidor UDP de Echo escutando em {host}:{port}...")

    while True:
        try:
            # Recebe dados e endereço do cliente
            mensagem, endereco = servidor.recvfrom(65535)  # Tamanho máximo UDP
            print(f"[{endereco}] Mensagem recebida: {mensagem.decode('utf-8')}")

            # Retorna a mensagem (eco)
            servidor.sendto(mensagem, endereco)
        except Exception as e:
            print(f"[!] Erro no servidor: {e}")

if __name__ == "__main__":
    main()
