# -*- coding: utf-8 -*-
import socket
import sys


def foward_lookup(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return False

def reverse_lookup(ip):
    try:
        #return socket.gethostbyaddr(ip)[0]
        return socket.gethostbyaddr(ip)
    except:
        return False
    
    
    