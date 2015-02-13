#!/usr/bin/env python

import sqlite3
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

sql = "SELECT * FROM stuffToPlot WHERE keyword = ? "
wordUsed = 'Python Sentiment'

graphArray = []

for row in c.execute(sql,[(wordUsed)]):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArray.append(splitInfo[2]+","+splitInfo[4])


datestamp,value = np.loadtxt(graphArray,delimiter=',',unpack=True,converters={ 0: mdate.strpdate2num(' %Y-%m-%d %H:%M:%S') })

fig = plt.figure()
rect = fig.patch

ax1 = fig.add_subplot(1,1,1,axisbg='white')
#TO plot with date
plt.plot_date(x=datestamp,y=value,fmt='b-',label='Value',linewidth=2)
plt.show()



