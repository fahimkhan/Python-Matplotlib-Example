#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

x = np.array([1,2,3,4,5,6,7,8,9,15])
y = np.array([1,2,8,12,15,17,66,121,233,211])

x_smooth = np.linspace(x.min(),x.max(),300)
y_smooth = spline(x,y,x_smooth)

plt.plot(x_smooth,y_smooth) #Smooth plot
plt.plot(x,y)               #Normal plot

plt.show()

