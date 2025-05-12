# cliente.py
# Participantes: Osiel Junior, Fernando Maia, Raul Rodrigues.



import socket  # Importa a biblioteca para comunicação via socket

def main():
    host = '127.0.0.1'  # IP do servidor (localhost para testes locais)
    port = 5000         # Porta onde o servidor está ouvindo

    try:
        # Cria um socket TCP/IP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta ao servidor
        cliente.connect((host, port))

        # Solicita uma mensagem do usuário
        mensagem = input("Digite uma mensagem para enviar ao servidor: ").strip()

        # Verifica se a mensagem é vazia
        if not mensagem:
            print("Mensagem vazia não é permitida.")
            cliente.close()
            return

        # Envia a mensagem para o servidor
        cliente.send(mensagem.encode('utf-8'))

        # Aguarda e imprime a resposta do servidor
        resposta = cliente.recv(1024).decode('utf-8')
        print("Resposta do servidor:", resposta)

    except Exception as e:
        # Caso ocorra erro na conexão
        print(f"[!] Erro de conexão: {e}")

    finally:
        # Encerra a conexão com o servidor
        cliente.close()

if __name__ == "__main__":
    main()
