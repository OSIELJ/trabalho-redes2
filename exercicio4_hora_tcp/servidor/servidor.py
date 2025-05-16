import socket
import logging
import threading
from datetime import datetime
import os

# Caminho absoluto da pasta onde o script atual está
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo ao script
log_path = os.path.join(base_dir, 'servidor.log')

# Configuração do log
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

# Configurações do servidor
HOST = 'localhost'
PORT = 7000  # Porta conforme exigido

# Função para lidar com cada cliente
def handle_client(conn, addr):
    logging.info(f"Nova conexão de {addr}")
    print(f"[+] Cliente conectado: {addr}")

    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            logging.info(f"Comando recebido de {addr}: {data}")

            if data.lower() == "hora":
                now = datetime.now().strftime("%H:%M:%S")
                conn.sendall(f"Hora atual: {now}\n".encode())
            elif data.lower() == "sair":
                conn.sendall("Encerrando conexão...\n".encode())
                break
            else:
                conn.sendall("Comando inválido. Use 'hora' ou 'sair'.\n".encode())

    except Exception as e:
        logging.error(f"Erro com {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Cliente desconectado: {addr}")
        logging.info(f"Conexão encerrada com {addr}")


# Cria o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[+] Servidor ouvindo em {HOST}:{PORT}")
logging.info(f"Servidor iniciado em {HOST}:{PORT}")

# Loop principal para aceitar conexões
while True:
    try:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
    except Exception as e:
        logging.error(f"Erro ao aceitar conexão: {e}")
