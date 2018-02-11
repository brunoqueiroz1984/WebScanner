'''
Created on 10 de fev de 2018

@author: Bruno 
'''
from urllib.request import urlopen
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urlopen(path + "robots.txt")
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

