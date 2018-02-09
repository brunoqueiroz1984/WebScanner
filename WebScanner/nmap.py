'''
Created on 9 de fev de 2018

@author: Bruno
'''
import os

def get_nmap(options, ip):
    command = 'nmap ' + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results