'''
Created on 2015. 7. 28.

@author: finger
'''
from ctypes.test.test_errno import threading
import time

class myThread (threading.Thread):
    def __init__ (self, host_seq, host,time_sc):
        threading.Thread.__init__(self);
        self.host_seq = host_seq;
        self.host = host;
        self.time_sc = time_sc;
        
    def run(self):
        print 'aaaa'+self.host_seq+" "+self.host
        time.sleep(self.time_sc);
        
        
thread1 = myThread("1","b",2);
thread1.start();
thread2 = myThread("2","b",10);
thread2.start();

