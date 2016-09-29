# -*- coding: UTF8 -*-
#import Liner
from Liner import Liner
from Item import Item
import time
from datetime import datetime, date
import xml.etree.ElementTree as ET

#https://wikidocs.net/42
def getItem(str):
    sline = str.split('sendData:');
    root = None
    type = "sendData";
    if(len(sline)<=1):
        sline = str.split('readData:')
        type="readData"
    if(len(sline)>1):
        root = ET.fromstring(sline[1])
    if root==None:
        return None;
    #항목 추가할부분 입맛대로 골라 넣으세욤~
    return Item(content=root.findall(".//send_time")[0].text,type=type)





while True:
    fname = date.today().strftime("%Y%m%d");
    f = open("d:\\BOARD_"+fname+".log", 'w')
    #https://docs.python.org/2/library/datetime.html
    print(fname)
    liner = Liner("D:\\omnicns\\project\\cbis\\source\\telecom_company\\2g\\skt\\nateair\\log\\nateair_log\\broad2\\out."+fname,"%m/%d %H:%M:%S");
    lines = liner.getLines();

    for atItem in lines :
        print(str(atItem.date.strftime("%m/%d %H:%M:%S")) + "  " + str(atItem.content));
        xmlItem = getItem(atItem.content)
        if(xmlItem!=None):
            f.write(str(atItem.date.strftime("%m/%d %H:%M:%S")) +"|"+str(xmlItem.type)+"|"+ xmlItem.content+"\n")
    f.close()
    time.sleep(10)#second







