# Exercício 3 – Chat em Rede (TCP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participantes:** Osiel Junior, Fernando Maia, Raul Rodrigues

## Objetivo
Implementar um sistema de chat em tempo real que permita a comunicação bidirecional entre dois clientes via protocolo TCP, utilizando threads para envio e recebimento simultâneo de mensagens.

## Funcionalidades Implementadas

### Servidor
- Escuta na porta `12345` (`0.0.0.0:12345`)
- Aceita conexões de dois clientes simultâneos
- Utiliza `threading` para lidar com múltiplos clientes
- Encaminha mensagens de um cliente para o outro em tempo real
- Encerra conexões com segurança ao receber o comando `"sair"`

### Cliente
- Conecta ao servidor TCP na porta `12345`
- Envia mensagens digitadas pelo usuário
- Exibe mensagens recebidas de outro cliente em tempo real
- Utiliza `threading` para envio e recebimento simultâneo
- Encerra o chat com o comando `"sair"`

## Requisitos
- Python 3.10 ou superior  
- Sistema Operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor
No terminal:
```bash
cd exercicio3_chat_tcp/servidor
python3 servidor.py

##depois inicie o arquivo
cd exercicio3_chat_tcp/cliente
python3 cliente.py

