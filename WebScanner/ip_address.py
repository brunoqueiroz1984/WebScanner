'''
Created on 9 de fev de 2018

@author: Bruno
'''
import socket

def get_ip_address(url):
    return socket.gethostbyname(url)

