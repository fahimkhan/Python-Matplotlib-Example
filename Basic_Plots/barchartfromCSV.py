#!/usr/bin/env python

from pylab import *

name = []
value = []

readFile = open('barchartdata.csv','r').read()
eachLine = readFile.split('\n')


for line in eachLine:
    nv=line.split(',')
    if len(nv) > 1:
        name.append(nv[0])
        value.append(float(nv[1]))
    else:
        pass

pos = arange(len(name)) + .5  #Num of bar .5 is spacing between bar
barh(pos,value,align = 'center',color='#b8ff5c') #barh for horizontal
yticks(pos,name)
xlabel('sentiment index')
ylabel('Candidates')
title('Prezdex')
grid(True)
show()


