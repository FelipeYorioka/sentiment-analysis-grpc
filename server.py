import grpc
from concurrent import futures
import sentiment_pb2
import sentiment_pb2_grpc

class SentimentClassifier(sentiment_pb2_grpc.SentimentClassifierServicer):
   def ClassifyText(self, request, context):
       text = request.text.lower()
       print("Recebi do cliente:", text)  
       positivos = ["bom", "ótimo", "maravilhoso", "amei", "gostei", "excelente"]
       negativos = ["ruim", "péssimo", "horrível", "odiei", "terrível"]
       for palavra in positivos:
           if palavra in text:
               return sentiment_pb2.TextResponse(sentiment="positivo")
       for palavra in negativos:
           if palavra in text:
               return sentiment_pb2.TextResponse(sentiment="negativo")
       return sentiment_pb2.TextResponse(sentiment="neutro")

def serve():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   sentiment_pb2_grpc.add_SentimentClassifierServicer_to_server(
       SentimentClassifier(), server
   )
   server.add_insecure_port('[::]:50051')
   server.start()
   print("Servidor rodando na porta 50051")
   server.wait_for_termination()

if __name__ == "__main__":
   serve()