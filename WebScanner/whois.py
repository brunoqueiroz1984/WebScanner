'''
Created on 10 de fev de 2018

@author: Bruno 
'''
import os

def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    return str(process.read()) 