# cliente.py
# Participantes: Osiel Junior, Fernando Maia, Raul Rodrigues.

import socket

def main():
    host = '127.0.0.1'  # IP do servidor
    port = 6000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.settimeout(5.0)  # Timeout para evitar travamento

    print("Digite mensagens para enviar (ou 'sair' para encerrar):")

    while True:
        try:
            mensagem = input("> ").strip()

            if not mensagem:
                print("Mensagem vazia não é permitida.")
                continue

            if mensagem.lower() == "sair":
                print("Encerrando cliente.")
                break

            if len(mensagem.encode('utf-8')) > 65507:
                print("Mensagem ultrapassa o limite do UDP (64 KB).")
                continue

            # Envia mensagem para o servidor
            cliente.sendto(mensagem.encode('utf-8'), (host, port))

            # Recebe resposta
            resposta, _ = cliente.recvfrom(65535)
            print("Eco do servidor:", resposta.decode('utf-8'))

        except socket.timeout:
            print("[!] Tempo de resposta esgotado (timeout).")
        except Exception as e:
            print(f"[!] Erro no cliente: {e}")
            break

    cliente.close()

if __name__ == "__main__":
    main()
