#!/usr/bin/env python

import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

sql = "SELECT * FROM stuffToPlot WHERE keyword = ? "
wordUsed = 'Python Sentiment'

def readData():
    for row in c.execute(sql,[(wordUsed)]):
        print row



