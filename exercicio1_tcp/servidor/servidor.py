# servidor.py
# Participantes: Osiel Junior, Fernando Maia, Raul Rodrigues.

import socket      # Biblioteca para comunicação com sockets
import threading   # Biblioteca para usar múltiplas threads (clientes simultâneos)



# Função que lida com cada cliente conectado
def handle_client(conn, addr):
    print(f"[+] Conexão recebida de {addr}")
    while True:
        try:
            # Recebe a mensagem do cliente
            mensagem = conn.recv(1024).decode('utf-8')
            if not mensagem:
                break  # Sai do loop se a mensagem estiver vazia

            # Imprime a mensagem no console do servidor
            print(f"[{addr}] Mensagem recebida: {mensagem}")

            # Envia uma resposta de confirmação ao cliente
            conn.send("Mensagem recebida".encode('utf-8'))

        except Exception as e:
            # Se ocorrer erro com o cliente, mostra no console
            print(f"[!] Erro com {addr}: {e}")
            break

    # Encerra a conexão com o cliente
    conn.close()
    print(f"[-] Conexão encerrada com {addr}")

# Função principal do servidor
def main():
    host = '0.0.0.0'  # Escuta em todas as interfaces de rede
    port = 5000       # Porta definida para o servidor

    # Cria o socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o socket ao host e porta
    servidor.bind((host, port))

    # Coloca o socket em modo de escuta
    servidor.listen()

    print(f"[+] Servidor TCP escutando em {host}:{port}...")

    while True:
        # Aceita uma nova conexão de cliente
        conn, addr = servidor.accept()

        # Cria uma nova thread para lidar com o cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
