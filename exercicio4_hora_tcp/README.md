# Exercício 4 – Servidor de Hora com Threads (TCP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participantes:** Osiel Junior, Fernando Maia, Raul Rodrigues

## Objetivo
Criar um servidor multithread que forneça a hora atual para múltiplos clientes simultaneamente via protocolo TCP.

## Funcionalidades Implementadas

### Servidor
- Escuta na porta 7000 (`localhost:7000`)
- Utiliza `threading` para lidar com múltiplos clientes simultaneamente
- Envia a hora atual no formato `"HH:MM:SS"` ao cliente
- Registra todas as conexões e mensagens em um arquivo de log (`servidor.log`)
- Continua funcionando mesmo que algum cliente cause erro

### Cliente
- Conecta ao servidor TCP na porta 7000
- Recebe e exibe a hora enviada pelo servidor
- Encerra a conexão após receber a hora

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
