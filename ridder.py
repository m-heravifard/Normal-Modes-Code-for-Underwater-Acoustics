'''
Created on 2014

@author: Heravi
'''
## module ridder
''' root = ridder(f,a,b,tol=1.0e-9).
The root must be bracketed in (a,b).
'''

from math import sqrt

def ridder(f,a,b,tol=1.0e-9): 
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa*fb > 0.0: print('Root is not bracketed')
    for i in range(100):
        c = 0.5*(a + b); fc = f(c)
        s = sqrt(fc**2 - fa*fb)
        if s == 0.0: return None
        dx = (c - a)*fc/s
        if fa < fb: dx = -dx
        x = c + dx; fx = f(x)
        
        if (b - a) < tol: return x

        if (b - a) > tol:
            if (fc * fx) < 0.0:
                if x < c:
                    a = x; b = c; fa = fx; fb = fc
                else:
                    a = c; b = x; fa = fc; fb = fx
            else:
                if x < c: b = x; fb = fx
                else: a = x; fa = fx 
    return None
    print ('Too many iterations')
    
    



    
