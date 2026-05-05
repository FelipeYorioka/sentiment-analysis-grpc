# sentiment-analysis-grpc
Sistema de classificação de sentimentos utilizando gRPC e Python para a disciplina de Sistemas Distribuídos.

🧠 Visão do Sistema
O sistema desenvolvido é composto por duas máquinas distintas que se comunicam através do protocolo gRPC:

Máquina A (Servidor): Responsável pelo processamento e classificação de sentimentos em positivo, negativo ou neutro.

Máquina B (Cliente): Responsável por enviar as requisições de texto para análise.

A comunicação ocorre via gRPC, utilizando mensagens estruturadas com Protocol Buffers através da porta 50051.

🛠️ Tecnologias Utilizadas
Python 3

gRPC & Protocol Buffers (proto3)

🚀 Instruções de Execução
1. Instalar dependências
Para rodar o projeto, é necessário instalar as bibliotecas do gRPC:

Bash
pip install grpcio grpcio-tools
2. Gerar arquivos de comunicação (Stubs)
Dentro da pasta do projeto, execute o comando abaixo para compilar o arquivo .proto e gerar os arquivos auxiliares de comunicação:

Bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sentiment.proto
3. Iniciar o Servidor (Máquina A)
Execute o comando para ligar o servidor:

Bash
python server.py
4. Iniciar o Cliente (Máquina B)
Certifique-se de que o IP no arquivo client.py aponta para o endereço do servidor e execute:

Bash
python client.py
Projeto desenvolvido para fins acadêmicos na disciplina de Sistemas Distribuídos.
