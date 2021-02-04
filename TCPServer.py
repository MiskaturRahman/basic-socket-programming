from socket import *  # To create a socket
serverName = '192.168.31.1'  # setting a serverName variable to 192.168.31.1
serverPort = 12000  # setting a serverPort variable to 12000

serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a socket
# Binding or assigning serverport to serverSocket
serverSocket.bind((serverName, serverPort))

serverSocket.listen(1)  # server is listening on port 1

print('The server is ready to receive')  # Show that server is ready to receive

while True:
    # Server is ready to accept connection from serverSocket
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)  # Server is ready to receive

    # shows socket address and receives input from client
    print('connection established', addr, sentence.decode())

    # Capitalized sentence received client server sent
    capitalizedSentence = sentence.upper()
    # sends capitalizedSentence output to socket
    connectionSocket.send(capitalizedSentence)
