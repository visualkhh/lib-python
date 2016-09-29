# -*- coding: UTF8 -*-
#import Liner
from Liner import Liner
from Item import Item
import time
from datetime import datetime, date
import xml.etree.ElementTree as ET
import re

#https://wikidocs.net/42
def getItem(str):
    type=None
    m = re.search('channelID\[258\]', str)
    if(m==None):
        return None
    else:
        type="channel"

    #항목 추가할부분 입맛대로 골라 넣으세욤~
    m = re.search('(?<=mesgID\[)\w+', str)
    return Item(content=m.group(0),type=type)





while True:
    fname = date.today().strftime("%Y%m%d");
    f = open("d:\\CBPP_"+fname+".log", 'w')
    #https://docs.python.org/2/library/datetime.html
    liner = Liner("D:\\omnicns\\project\\cbis\\source\\telecom_company\\2g\\skt\\nateair\\log\\nateair_log\\newcbpp\\out."+fname,["%m-%d %H:%M:%S","%m/%d %H:%M:%S"]);
    lines = liner.getLines();

    for atItem in lines :
        print(str(atItem.date.strftime("%m/%d %H:%M:%S")) + "  " + str(atItem.content));
        atContent = getItem(atItem.content)
        if(atContent!=None):
            f.write(str(atItem.date.strftime("%m/%d %H:%M:%S")) +"|"+ atContent.content+"\n")
    f.close()
    time.sleep(10)#second








