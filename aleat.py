#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random
import sys


class Aleat(webapp.webApp):
    def process(self, parsedRequest):
        newURL = str(random.randint(0, 10000))
        htmlAnswer = "<html><body><p>Hola. <a href=" + newURL + ">Dame otra"
        htmlAnswer = htmlAnswer + "</a></p></body></html>"
        return ("200 OK", htmlAnswer)

if __name__ == '__main__':
    try:
        aleat = Aleat("localhost", 9999)
    except KeyboardInterrupt:
        sys.exit()
