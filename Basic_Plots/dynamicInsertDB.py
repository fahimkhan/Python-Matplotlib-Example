#!/usr/bin/env python

import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def createTable():
    c.execute("CREATE TABLE stuffToPlot (ID INT,unix REAL,datestamp TEXT,keyword TEXT,value REAL)")


 
idfordb = 5
keyword = 'Python sentiment'
value = 7



def dataEntry():
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO stuffToPlot(ID,unix,datestamp,keyword,value) VALUES(?,?,?,?,?)",(idfordb,time.time(),date,keyword,value))
    conn.commit()


