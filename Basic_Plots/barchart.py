#!/usr/bin/env python

from pylab import *

pos = arange(6) + .5  #Num of bar .5 is spacing between bar

barh(pos,(3,5,2,1,2,9),align = 'center',color='#b8ff5c') #barh for horizontal
yticks(pos,('Rand Paul','Hillary','Obama','Jhon','James','Khan'))
xlabel('sentiment index')
ylabel('Candidates')
title('Prezdex')
grid(True)
show()


