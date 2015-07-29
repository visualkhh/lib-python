# -*- coding: utf-8 -*-
import os
import sys
from khh.py27.communication.network.util.NetWorkUtil import *


import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","javadev","search" )

# prepare a cursor object using cursor() method
cursor = db.cursor()






site_list =[
            ["A001" ,"KB국민은행"],
            ["A002" ,"우리은행"],
            ["A003" ,"신한은행"],
            ["A004" ,"하나은행"],
            ["A005" ,"스탠다드차타드은행"],
            ["A006" ,"한국씨티은행"],
            ["A007" ,"외환은행"],
            ["A008" ,"대구은행"],
            ["A009" ,"부산은행"],
            ["A010" ,"광주은행"],
            ["A011" ,"경남은행"],
            ["A012" ,"전북은행"],
            ["A013" ,"제주은행"],
            ["A014" ,"농협"],
            ["A015" ,"수협"],
            ["A016" ,"한국산업은행"],
            ["A017" ,"기업은행"],
            ["A018" ,"신협"],
            ["A019" ,"우체국"],
            ["A020" ,"새마을금고"],
            ["C001" ,"신한카드"],
            ["C002" ,"광주카드"],
            ["C003" ,"롯데카드"],
            ["C004" ,"삼성카드"],
            ["C005" ,"씨티카드"],
            ["C006" ,"전북카드"],
            ["C007" ,"하나카드"],
            ["C008" ,"현대카드"],
            ["C009" ,"BC카드"],
            ["C010" ,"KB카드"],
            ["C011" ,"NH카드"],
            ["E001" ,"홈택스(국세청)"],
            ["E002" ,"케이노트"],
            ["E003" ,"센드빌"],
            ["E004" ,"스마트빌"],
            ["E005" ,"트러스빌"],
            ["E006" ,"세무로"],
            ["E007" ,"WebTax21"],
            ["E008" ,"Billmate"],
            ["E009" ,"다큐빌"],
            ["E010" ,"TaxBill365"],
            ["E011" ,"Bill36524"],
            ["E012" ,"유노트"],
            ["E013" ,"서울외국환중개"],
            ["E014" ,"외환은행 환율"],
            ["E015" ,"한국은행경제통계시스템"],
            ["E016" ,"KOFIA BIS 경제지표"],
            ["E017" ,"여신금융협회 장부관리"],
            ["E018" ,"하이웍스빌 장부관리(전자세금계산서발행)"],
            ["E019" ,"세틀뱅크 가상계좌"],
            ["E020" ,"한국증권금융"],
            ["E021" ,"HSBC Direct"],
            ["E022" ,"신한금융투자"],
            ["E023" ,"신영증권"],
            ["E024" ,"우리투자증권"],
            ["E025" ,"유안타증권"],
            ["F001" ,"핑거"],
            ["F002" ,"인사이드뱅크 업데이트더존 업데이트 서버"],
            ["F003" ,"인사이드뱅크 더존 공지사항 서버"],
            ["S001" ,"nprotect"],
            ["S002" ,"안랩"],
            ["S003" ,"소프트캠프"],
            ["S004" ,"라온시큐어"],
            ["S005" ,"initech"],
            ["S006" ,"nsmartad"],
            ["S007" ,"nsmartad"],
            ["S008" ,"verisign"],
            ["S009" ,"cyveillance"],
            ["S010" ,"symcd"],
            ["S011" ,"digicert"],
            ["I001" ,"아이퀘스트"]
            ]


for atSite in site_list: 
    site_seq = atSite[0].strip();
    name = atSite[1].strip();
    #print(site_seq+"  "+name)
    query = 'INSERT INTO SITE VALUES("'+site_seq+'","'+name+'");';
    print(query)
    #cursor.execute(query);


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
 