'''
Created on 2015. 6. 23.

@author: Administrator
'''
from grab import Grab
import logging

logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.go('https://github.com/login')
g.set_input('login', '***')
g.set_input('password', '***')
g.submit()
g.doc.save('./x.html')
