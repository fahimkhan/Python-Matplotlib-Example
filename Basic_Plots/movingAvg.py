#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from numpy import convolve

"""

A widely used indicator in technical analysis that helps smooth out price action by filtering out the noise from random price fluctuations. 
A moving average MA is a trend-following or lagging indicator because it is based on past prices. 
The two basic and commonly used MAs are the simple moving average SMA, which is the simple average of a security over a defined number of time periods, and the exponential moving average (EMA), which gives bigger weight to more recent prices.
The most common applications of MAs are to identify the trend direction and to determine support and resistance levels. 
While MAs are useful enough on their own, they also form the basis for other indicators such as the Moving Average Convergence Divergence (MACD).
"""


def movingaverage(values,window):
    weigths = np.repeat(1.0,window)/window
    sma = np.convolve(values,weigths,'valid')
    return sma

x = [1,2,3,4,5,6,7,8,9,10]
y = [3,5,1,6,2,1,6,1,9,2]

yMA = movingaverage(y,3)

print yMA

plt.plot(x[len(x)-len(yMA):],yMA)  #Simple moving Avg Plot
plt.show()
