# sentiment-analysis-grpc

Sistema de classificação de sentimentos utilizando gRPC e Python para a disciplina de Sistemas Distribuídos.

## 🧠 Visão do Sistema
O sistema desenvolvido é composto por duas máquinas distintas que se comunicam através do protocolo gRPC:

- **Máquina A (Servidor):** Responsável pelo processamento e classificação de sentimentos em positivo, negativo ou neutro.
- **Máquina B (Cliente):** Responsável por enviar as requisições de texto para análise.

A comunicação ocorre via gRPC, utilizando mensagens estruturadas com Protocol Buffers através da porta 50051.

## 🛠️ Tecnologias Utilizadas
- Python 3
- gRPC & Protocol Buffers (proto3)

---

## 🚀 Instruções de Execução

### 1. Instalar dependências
Para rodar o projeto, é necessário instalar as bibliotecas do gRPC:

```bash
pip install grpcio grpcio-tools
