# Exercício 4 – Servidor de Hora com Threads (TCP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participantes:** Osiel Junior, Fernando Maia, Raul Rodrigues

## Objetivo
Criar um servidor multithread que forneça a hora atual para múltiplos clientes simultaneamente via protocolo TCP.

##  Funcionalidades Implementadas

###  Servidor
- Roda na porta `7000` (`localhost:7000`)
- Aceita múltiplos clientes simultaneamente usando threads
- Mantém a conexão ativa com o cliente enquanto ele envia comandos
- Responde aos seguintes comandos:
  - `hora` → envia a hora atual no formato `"HH:MM:SS"`
  - `sair` → encerra a conexão com o cliente
- Retorna uma mensagem de erro para comandos inválidos
- Gera logs detalhados no arquivo `servidor.log` com:
  - Conexões iniciadas
  - Comandos recebidos
  - Conexões encerradas

### Cliente
- Conecta-se ao servidor e mantém a conexão ativa
- Permite que o usuário envie comandos via teclado:
  - `hora` → recebe e exibe a hora atual
  - `sair` → encerra a conexão
- Exibe as respostas do servidor em tempo real

## Requisitos
- Python 3.10 ou superior
- Sistema Operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor
No terminal:
```bash
cd exercicio4_hora_tcp/servidor
python3 servidor.py

##depois inicie o arquivo
cd exercicio4_hora_tcp/cliente
python3 cliente.py
