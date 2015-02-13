#!/usr/bin/env python

import matplotlib.pyplot as plt


   
def graphPlot():
    x = [] 
    y = []

    readFile = open('data.txt','r') #Read file
    sepFile = readFile.read().split('\n')  #Read data
    readFile.close()

    #Customizatio
    fig = plt.figure()  #Define figure
    rect = fig.patch
    rect.set_facecolor('blue')  ##U can give Hex code also

    for plotPair in sepFile:
        XY = plotPair.split(',')
        if len(XY) > 1:    #For null value in your file
            x.append(int(XY[0]))
            y.append(int(XY[1]))
        else:
            pass

    
    #With Figure
    ax1 = fig.add_subplot(1,1,1,axisbg='grey') #First 1,1 is "1 by 1" and chart No:1
    ax1.plot(x,y,'c',linewidth=2.5)
    ax1.set_title('Title')
    ax1.set_xlabel('X-label')
    ax1.set_ylabel('Y-label')


    plt.show()



    ##Without figure
    '''
    plt.plot(x,y)  #Always Equal no of X and Y
    plt.title('Plot from File')
    plt.xlabel('X-label')
    plt.ylabel('Y-label')
    plt.show()

    '''
graphPlot()
