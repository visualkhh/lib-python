# -*- coding: utf-8 -*-
import os
import sys
from khh.py27.communication.network.util.NetWorkUtil import *


import MySQLdb




host_list = set();
f = open("./host_list.txt","r");
lines = f.readlines()
for atline in lines :
    print (atline);
    host_list.add(atline);





# Open database connection
db = MySQLdb.connect("localhost","root","javadev","search" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
cnt = 0 ;
for atHost in host_list: 
    print(atHost.strip())
    cnt+=1;
    query = 'INSERT INTO HOST VALUES('+str(cnt)+',"'+atHost.strip()+'")';
    print(query)
    cursor.execute(query);


# execute SQL query using execute() method.

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print "Database version : %s " % data

# disconnect from server
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
 