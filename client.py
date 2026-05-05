import grpc
import sentiment_pb2
import sentiment_pb2_grpc

# Lembre-se: se for testar em computadores diferentes, 
# troque 'localhost' pelo IP da Máquina A
channel = grpc.insecure_channel('localhost:50051')
stub = sentiment_pb2_grpc.SentimentClassifierStub(channel)

texts = [
    "eu amei esse produto",
    "esse produto é ruim",
    "experiência maravilhosa",
    "atendimento péssimo",
    "gostei bastante",
    "não recomendo"
]

for text in texts:
    response = stub.ClassifyText(sentiment_pb2.TextRequest(text=text))
    print("Texto:", text)
    print("Sentimento:", response.sentiment)
    print("------")