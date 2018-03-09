#!/usr/bin/python3
"""
Simple HTTP Server: serves random URLs usign a hyperlink

Rodrigo Pacheco Martinez-Atienza
r.pachecom @ gsyc.es
SAT subject (Universidad Rey Juan Carlos)
"""

import socket
import random
import webapp


def parse:
    try:
        method = received.split()[0]
        resource = received.split()[1]
        return(method, resource)
    except:
        return('', '')

def process:
    rnd_num = random.randint(1, 9999999)
    return ("200 OK", "<html><body><h1>Hola!</h1>" +
                      "<a href=" + str(rnd_num) + ">Dame otra</a>" +
                      "</body></html>")

if __name__ == "__main__":

try:
    while True:
        myApp = webapp()
        # print('Waiting for connections')
        # (recvSocket, address) = mySocket.accept()
        # print('Request received:')
        # print(recvSocket.recv(2048))
        # print('Answering back...')
        #
        # rnd_num = random.randint(1, 9999999)
        #
        # recvSocket.send(bytes(
        #                 "HTTP/1.1 200 OK\r\n\r\n" +
        #                 "<html><body><h1>Hola!</h1>" +
        #                 "<a href=" + str(rnd_num) + ">Dame otra</a>" +
        #                 "</body></html>" +
        #                 "\r\n", "utf-8"))
        # recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
