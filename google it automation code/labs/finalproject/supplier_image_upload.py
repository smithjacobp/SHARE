#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for filething in os.listdir("./supplier-data/images"):
    if filething.endswith(".jpeg"):
        with open('./supplier-data/images/' + filething, 'rb') as openedfile:
            send = requests.post(url, files={'file': openedfile})
            
#rb is read binary mode which you need to open images as byte objects instead of string objects
#the rest is just normal syntax
