import time
from datetime import datetime, date, time
from Item import Item
import types


class Liner:
    def __init__(self, filepath, dateFormat):
        self.filepath = filepath
        self.dateFormat = dateFormat;

    def getLines(self):
        result = []
        f = open(self.filepath,"r");
        lines = f.readlines()

        for atline in lines :
            atDate = self.pasingDate(atline);
            if(atDate!=None):
                result.append(Item(atDate ,atline))
            else:
                #print(result[-1])
                result[-1].setContent(result[-1].getContent()+str(atline))
                #result[-1] = str(result[-1])+str("")+str(atline)

        f.close();
        return result;

    def pasingDate(self,line):
        #print (type(self.dateFormat))
        #print (isinstance(self.dateFormat, types.StringTypes))
        dt = None
        if type(self.dateFormat) is list:
            dt = None
            for atDateFormat in self.dateFormat:
                dt = self.getDate(line, atDateFormat);
                if dt!=None:
                    break
        else:
            if(dt==None):
                dt = self.getDate(line, self.dateFormat)
        return dt






    def getDate(self, line, dateFormat):
        sline = line.split('->');
        dt = None
        try:
            #https://docs.python.org/2/library/datetime.html
            dt = datetime.strptime(sline[0], dateFormat)  #09/21 23:57:01
        except :
            dt = None
        return dt
