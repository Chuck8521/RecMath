# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:05:41 2019

@author: ckuli
"""


from copy import deepcopy
import operator as op
from functools import reduce
import math


def ncr(n, r):
    
    if n < r:
        return 0
    
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def distt(a,b):
    return math.sqrt(((a - b)**2))

def genOrdering(a, points):
    
    ordering = []
    dists = []
    tdists = []
    
    for p in points:
        dists.append(distt(a,p))
        tdists.append(distt(a,p))
        
        
    while len(tdists) > 0:
        minD = min(tdists)
        ordering.append(dists.index(minD))
        tdists.remove(minD)
    
    return ordering


n = 4

MAX = 15

pastC = [ [] for _ in range(MAX)]

pastC[3] = [[1,2,3]]


while n < MAX:
    
    cs = []
    
    basicConfig = pastC[n - 1][0]
    #print(basicConfig)
    finalP = n
    
    for i in range(n - 2):
        q = deepcopy(basicConfig)
        #print("hi")
        q.append(finalP)
        cs.append(q)
        #print(q)
        finalP += 1
        
    #Simple increments are done.
    
    #One complex increment per other previous config.

    finalP -= 1 #For lower portion, adjust for the final "error" increment.  
    
    
    lastConfigs = pastC[n - 1]
    
    dist = 0
    
    for i in range(len(lastConfigs)):
        
        if i == 0:
            pass
            #We did all of these already.
        else:
            
            thisC = lastConfigs[i]
            
            #Find the appropriate number to shift the n-th point by.
            
            lastC = lastConfigs[i - 1]
            
            
            for j in range(len(lastC)):
                dist += abs(thisC[j] - lastC[j])
                
                
            qq = deepcopy(thisC)
            qq.append(finalP + dist)
            cs.append(qq)
    
    
    
    
    
    
    
    pastC[n] = cs
    
    
    
    
    
    
    
    
    
    
    n += 1
    
    
    
    
    
    
    
    
    









print(pastC)
    












#Verify correctness.

#For each entry in pastC[n], there should be 2n-2 -> ncr(n,2) + 1 orderings, in order.

wrong = False

for i in range(len(pastC)):
    
    configs = pastC[i]
    
    expectedOrderings = 2 * i - 2
    
    for c in configs:
        
        
        #if numOrders != expected, print wrong
        
        #Calculate numOrders.
        
        vPoint = -1
        
        orders = []
        
        while vPoint < c[len(c) - 1] + 1:
            
            ar = genOrdering(vPoint,c)
            
            if ar not in orders:
                orders.append(ar)
            
            vPoint += 0.01
        
        
        if len(orders) != expectedOrderings:
            wrong = True
        """    print("Wrong.")
        else:
            print("Right.")"""
        
        
        
        
        
        
        expectedOrderings += 1





if wrong:
    print("Something failed.")
else:
    print("Everything is correct.")

    
    
    
    
    
    
    
    
    
    
    
