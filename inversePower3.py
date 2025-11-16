'''
Created on 2014

@author: Heravi
'''
## module inversePower3
''' lam,x = inversePower3(d,c,s,tol=1.0e-6).
Inverse power method applied to a symmetric tridiagonal matrix.
eigenvalues and the corresponding eigenvector.
'''
from LUdecomp3 import *
from math import sqrt
from numpy import dot, ones

def inversePower3(d,c,s,tol=1.0e-6):
    n = len(d)
    e = c
    dStar = d - s # Form [A*] = [A] - s[I]
    c,dStar,e = LUdecomp3(c,dStar,e) # Decompose [A*]
    x = ones(n) # Seed x with ones numbers
    xMag = sqrt(dot(x,x)) # Normalize [x]
    x =x/xMag
    flag = 0
    for i in range(6500000): # Begin iterations
        xOld = x.copy() # Save current [x]
        x = LUsolve3(c,dStar,e,x) # Solve [A*][x] = [xOld]
        xMag = sqrt(dot(x,x)) # Normalize [x]
        x = x/xMag
        if dot(xOld,x) < 0.0: # Detect change in sign of [x]
            sign = -1.0
            x = -x
        else: sign = 1.0
        if sqrt(dot(xOld - x,xOld - x)) < tol:
            return s + sign/xMag,x
    print('Inverse power method did not converge')
    
   
   


