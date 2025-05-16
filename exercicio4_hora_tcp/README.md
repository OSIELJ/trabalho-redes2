
# Exercício – Servidor de Hora com Múltiplos Clientes (TCP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participantes:** Osiel Junior, Fernando Maia, Raul Rodrigues

##  Objetivo
Implementar um servidor multithread que forneça a hora atual para múltiplos clientes simultaneamente via protocolo TCP.

---

##  Funcionalidades Implementadas

### Servidor
- Roda na porta `7000` (`localhost:7000`)
- Utiliza **threads** para atender múltiplos clientes em paralelo
- Envia a hora atual no formato `"HH:MM:SS"` para cada cliente ao se conectar
- Registra logs em arquivo (`servidor.log`) para cada conexão recebida e encerrada
- Lida com falhas de clientes sem derrubar o servidor

###  Cliente
- Conecta-se ao servidor via TCP
- Solicita e exibe a hora recebida uma única vez no console

---

##  Requisitos
- Python 3.10 ou superior
- Sistema Operacional: Linux ou Windows (testado no Ubuntu)
- Editor recomendado: Visual Studio Code

---

##  Como Executar

### 1. Iniciar o servidor
```bash
cd servidor
python3 servidor.py

##  Como iniciar um ou mais clientes
cd cliente
python3 cliente.py


