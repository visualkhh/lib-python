import time
from datetime import datetime, date, time

class Item:
    def __init__(self, date=None, content=None, type=None):
        self.date = date
        self.content = content;
        self.type = type;

    def getDate(self):
        return self.date;

    def getContent(self):
        return self.content;

    def setDate(self,date):
        self.date = date;

    def setContent(self,content):
        self.content = content;

    def getType(self):
        return self.type;

    def setType(self,type):
        self.type = type;
