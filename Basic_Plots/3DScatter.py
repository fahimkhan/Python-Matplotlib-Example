#!/usr/bin/env python

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

X = [1,2,3,4,5,6,7,8,9,10]
Y = [4,5,6,7,8,9,1,2,3,10]
Z = [10,7,8,9,5,4,6,3,2,1]

ax.scatter(X,Y,Z,c='r',marker='o')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

plt.show()

