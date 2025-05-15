# Exercício 2 – Servidor Echo (UDP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participantes:** Osiel Junior, Fernando Maia, Raul Rodrigues

## Objetivo
Desenvolver um cliente e um servidor que se comuniquem usando o protocolo UDP, com funcionalidade de eco (retorno da mensagem enviada).

## Funcionalidades Implementadas

### Servidor
- Escuta na porta 6000 (`0.0.0.0:6000`)
- Recebe mensagens dos clientes
- Exibe cada mensagem recebida no console
- Retorna a mesma mensagem ao cliente (eco)

### Cliente
- Envia mensagens ao servidor via UDP
- Exibe a resposta (eco) recebida
- Valida mensagens vazias
- Impede envio de mensagens maiores que 64 KB (limite UDP: 65507 bytes)
- Permite envio contínuo até o comando `"sair"`
- Trata perda de pacotes com timeout de 5 segundos

## Requisitos
- Python 3.10 ou superior
- Sistema Operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor
No terminal:
```bash
cd exercicio2_udp_echo
python3 servidor/servidor.py

##depois inicie o arquivo
python3 cliente/cliente.py
