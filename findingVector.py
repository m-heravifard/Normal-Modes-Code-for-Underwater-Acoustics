'''
@author: Mohammad E. Heravifard
Supervisor: Prof. Parviz Ghadimi
'''
from math import sqrt
#from numpy import dot
from LUdecomp3 import *
#from Main import *
from h7 import *


#d = [-1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -1.6326905417814508, -0.81634527089072539]

#c = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


Finallambdas = range(n)

for i in range(n):
    Finallambdas[i] = lambdas1[i]
    
#print Finallambdas

xx = []
for i in range(N):
    xx.append(range(N))
    
b = []
for i in range(N):
    b.append(0.0000000000000000000000000000000000000000000001)

    
    
#def EigenVector(dprim,cprim,s):
#    eprim = cprim
#    dstarprim = dprim - s
#    
#    cprim,dstarprim,eprim = LUdecomp3(cprim,dstarprim,eprim) # Decompose [A*]
#    xprim = LUsolve3(cprim,dstarprim,eprim,b)
#    return xprim


dprim = d
cprim = c
dstarprim = dprim
    
for i in range(N):
    s = Finallambdas[i]
    eprim = cprim
    dstarprim[i] = dprim[i] - s
    cprim,dstarprim,eprim = LUdecomp3(cprim,dstarprim,eprim) # Decompose [A*]
    xprim = LUsolve3(cprim,dstarprim,eprim,b)
    xMag = sqrt(dot(xprim,xprim)) # Normalize [xprim]
    print xMag
    for k in range(N):
        xprim[k] = xprim[k]/xMag
    #xprim = EigenVector(dprim,cprim,s)
    for j in range(N):
        xx[i][j] = xprim[j]
               
print xx









    

