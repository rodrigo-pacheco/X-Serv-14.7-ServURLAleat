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

class myApp(webapp.webApp)
    def parse(self, request):
        try:
            method = received.split()[0]
            resource = received.split()[1]
            return(method, resource)
        except:
            return('', '')

    def process(parsedRequest):
        rnd_num = random.randint(1, 9999999)
        return ("200 OK", "<html><body><h1>Hola!</h1>" +
                          "<a href=" + str(rnd_num) + ">Dame otra</a>" +
                          "</body></html>")

if __name__ == "__main__":
    myApp = webapp.webApp("localhost", 1234)
