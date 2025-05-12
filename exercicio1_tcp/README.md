# Exercício 1 – Cliente/Servidor TCP

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participantes:** Osiel Junior, Fernando Maia, Raul Rodrigues

## Objetivo
Implementar um cliente e um servidor que se comuniquem via protocolo TCP, permitindo o envio e recebimento de mensagens com validação e múltiplos clientes.

## Funcionalidades Implementadas

### Servidor
- Escuta na porta 5000 (`0.0.0.0:5000`)
- Aceita conexões de múltiplos clientes com `threading`
- Imprime as mensagens recebidas no console
- Responde com a mensagem `"Mensagem recebida"`
- Encerra conexões com segurança

### Cliente
- Conecta ao servidor TCP na porta 5000
- Envia uma mensagem digitada pelo usuário
- Valida mensagens vazias (não permite envio)
- Exibe a resposta do servidor
- Encerra a conexão corretamente

## Requisitos
- Python 3.10 ou superior
- Sistema Operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor
No terminal:
```bash
cd exercicio1_tcp
python3 servidor/servidor.py
