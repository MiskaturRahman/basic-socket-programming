from socket import *
import random

QotD = ["Love For All, Hatred For None.", "Change the world by being yourself.", "Every moment is a fresh beginning.", "Everything you can imagine is real.", "Simplicity is the ultimate sophistication.",
        "All limitations are self-imposed.", "Tough times never last but tough people do.", "Yesterday you said tomorrow. Just do it.", "It hurt because it mattered."]

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The QotD server is ready.')

while True:
    randQotD = random.randint(0, len(QotD)-1)
    print("Randomly picked quote:"+QotD[randQotD])
    data, addr = serverSocket.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message: %s" % data)
    print(f"IP Address: {addr}")
    serverSocket.sendto(QotD[randQotD].encode(), addr)  # reply with quote
