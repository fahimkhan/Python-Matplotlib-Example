#!/usr/bin/env python

import matplotlib.pyplot as plt


   
def graphPlot():
    x1 = [] 
    y1 = []

    readFile1 = open('data1.txt','r') #Read file
    sepFile1 = readFile1.read().split('\n')  #Read data
    readFile1.close()

    x2 = [] 
    y2 = []

    readFile2 = open('data2.txt','r') #Read file
    sepFile2 = readFile2.read().split('\n')  #Read data
    readFile2.close()
    
    #Customizatio
    
    fig = plt.figure()  #Define figure
    rect = fig.patch
    rect.set_facecolor('blue')  ##U can give Hex code also

    for plotPair in sepFile1:
        XY = plotPair.split(',')
        if len(XY) > 1:    #For null value in your file
            x1.append(int(XY[0]))
            y1.append(int(XY[1]))
        else:
            pass

    for plotPair in sepFile2:
        XY = plotPair.split(',')
        if len(XY) > 1:    #For null value in your file
            x2.append(int(XY[0]))
            y2.append(int(XY[1]))
        else:
            pass
    
    #With Figure
    ax1 = fig.add_subplot(2,1,1,axisbg='grey') #First 1,1 is "1 by 1" or "Height by Width" and chart No:1 
    ax1.plot(x1,y1,'c',linewidth=2.5)
    ax1.tick_params(axis='x',color='c')  #managing ticks
    ax1.tick_params(axis='y',color='c')
    #Some CSS work at the border area
    ax1.spines['bottom'].set_color('w')
    ax1.spines['top'].set_color('w')
    ax1.spines['left'].set_color('w')
    ax1.spines['right'].set_color('w')
    ax1.yaxis.label.set_color('c')
    ax1.xaxis.label.set_color('c')
    ax1.set_title('Title',color='c')
    ax1.set_xlabel('X-label')
    ax1.set_ylabel('Y-label')

    ax2 = fig.add_subplot(2,1,2,axisbg='grey') #First 1,1 is "1 by 1" and chart No:1
    ax2.plot(x2,y2,'c',linewidth=2.5)
    ax2.tick_params(axis='x',color='c')  #managing ticks
    ax2.tick_params(axis='y',color='c')
    #Some CSS work at the border area
    ax2.spines['bottom'].set_color('w')
    ax2.spines['top'].set_color('w')
    ax2.spines['left'].set_color('w')
    ax2.spines['right'].set_color('w')
    ax2.yaxis.label.set_color('c')
    ax2.xaxis.label.set_color('c')
    ax2.set_title('Title',color='c')
    ax2.set_xlabel('X-label')
    ax2.set_ylabel('Y-label')

    plt.show()



graphPlot()
