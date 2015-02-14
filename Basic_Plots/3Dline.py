#!/usr/bin/env python

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

X,Y,Z = [1,2,3,4,5,6,7,8,9,10],[4,5,6,7,8,9,1,2,3,10],[10,7,8,9,5,4,6,3,2,1]

ax.plot_wireframe(X,Y,Z)

plt.show()

