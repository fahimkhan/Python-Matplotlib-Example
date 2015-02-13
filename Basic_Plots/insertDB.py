#!/usr/bin/env python

import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def createTable():
    c.execute("CREATE TABLE stuffToPlot (ID INT,unix REAL,datestamp TEXT,keyword TEXT,value REAL)")


def dataEntry():
    c.execute("INSERT INTO stuffToPlot VALUES(1,132456761.256,'2015-02-01 10:09:50','Python Sentiment',5)")
    c.execute("INSERT INTO stuffToPlot VALUES(2,1356761.6,'2015-02-01 10:09:50','Python Sentiment',6)")
    c.execute("INSERT INTO stuffToPlot VALUES(3,2456761.25,'2015-01-10 10:50:50','Python Sentiment',3)")
    c.execute("INSERT INTO stuffToPlot VALUES(4,6761.56,'2015-02-02 10:40:50','Python Sentiment',4)")
    conn.commit()


