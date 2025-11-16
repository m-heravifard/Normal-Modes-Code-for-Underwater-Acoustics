'''
Created on 2014

@author: Heravi
'''


from numpy import *

'''xData = array([3, 5, 8, 12])
yData = array([4, 13, 20, 50])
x = 0.0'''

def neville(xData,yData,x):
    m = len(xData) # number of data points
    y = yData
    for k in range(1,m):
        for i in range(m-k):
            y[i] = ((x - xData[i+k])*y[i] + (xData[i] - x)*y[i+1])/ \
            (xData[i]-xData[i+k])
    return y[0]


#print neville(xData,yData,x)