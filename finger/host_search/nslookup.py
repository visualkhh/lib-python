# -*- coding: utf-8 -*-
import os
import sys
import time
from khh.py27.communication.network.util.NetWorkUtil import *
from ctypes.test.test_errno import threading

import MySQLdb





class NsLookUp (threading.Thread):
    def __init__ (self, thread_name, host_seq, host):
        threading.Thread.__init__(self);
        self.thread_name = thread_name;
        self.host_seq   = host_seq;
        self.host       = host;
        print (self.thread_name+"] START::  "+self.host_seq+" "+self.host+"");
        
    def run(self):
        loopCnt = 150;
        sleeptime = 3;
        setval = set();
        for at in range(loopCnt):
            url_ip = foward_lookup(self.host);
            print(self.thread_name+"] LOOP::  "+self.host_seq+"("+self.host+") result:"+ str(url_ip) + "    cnt:"+str(at))
            if url_ip==False:
                break;
            setval.add(url_ip)
            if at==5 and len(setval)==1:
                print("break")
                break
            time.sleep(sleeptime)
            
        if len(setval)>0 :
            db = MySQLdb.connect("localhost","root","javadev","search" );
            cursor = db.cursor()
            ip_seq=0;
            for atSet in setval:
                ip_seq+=1;
                #NsLookUp(host_seq, ip_seq, atSet).start();
                query = 'INSERT INTO IP VALUES('+self.host_seq+','+str(ip_seq)+', "'+atSet+'")';
                print(query)
                cursor.execute(query);
                db.commit();
            db.close()

        











# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print "Database version : %s " % data

# disconnect from server


# Open database connection
db = MySQLdb.connect("localhost","root","javadev","search" )
# prepare a cursor object using cursor() method

cursor = db.cursor()
query = "SELECT HOST_SEQ, HOST FROM HOST";
print(query)

cursor.execute(query)
data = cursor.fetchall();
cnt=0;
for row in data :
    cnt+=1;
    host_seq = str(row[0]);
    host     = str(row[1]);
    print(host_seq+"   "+host)
    NsLookUp("thread-"+str(cnt), host_seq, host).start();
    #time.sleep(1);
    

        



db.commit();
db.close()
#scriptpath = "./khh/py27/communication/network/util/NetWorkUtil.py"
# Add the directory containing your module to the Python path (wants absolute paths)
#sys.path.append(os.path.abspath(scriptpath))

#ip = foward_lookup("ahnlabdownload.nefficient.co.kr");
#print ip
#ip = foward_lookup("ahnlabdownload.nefficient.co.kr");
#print ip
#ip = foward_lookup("ahnlabdownload.nefficient.co.kr");
#print ip
#ip = foward_lookup("ahnlabdownload.nefficient.co.kr");
#print ip
 