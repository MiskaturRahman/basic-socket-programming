from socket import *  # To create a socket
serverName = '127.0.0.1'  # setting a serverName variable to 127.0.0.1
serverPort = 12000  # setting a serverPort variable to 12000
clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a socket
# Binding or assigning serverport to serverSocket

clientSocket.connect((serverName, serverPort))  # initiates TCP connection

# prompt user to input lowercase sentence
sentence = input('input lowercase sentence: ')
# send sentence to TCP connection through client socket
clientSocket.send(sentence.encode())
# receives modified sentence from server
modifiedSentence = clientSocket.recv(1024)

print('From server', modifiedSentence.decode())  # prints modified sentence

clientSocket.close()  # closes socket and TCP connection
