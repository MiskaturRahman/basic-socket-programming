from socket import *
serverPort = 12000

message = "Please send me a quote."
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(), ("192.168.1.15", serverPort))
QotD, addr = clientSocket.recvfrom(1024)
print(QotD.decode())
