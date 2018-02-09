'''
Created on 9 de fev de 2018

@author: Bruno
'''
import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)
