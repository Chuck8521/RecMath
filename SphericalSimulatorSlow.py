# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:19:04 2019

@author: ckuli
"""


#(r,theta,phi)

r = 1
n = 0
numPointsToSim = 50000000


import math
import random



def isclose(a,b,sig_fig=5):
    return (a==b or int(a*10**sig_fig) == int(b*10**sig_fig))

def dist(a,b):
    
    theta1 = a[1]
    phi1 = a[2]
    x1 = math.cos(theta1)*math.sin(phi1)
    y1 = math.sin(theta1)*math.sin(phi1)
    z1 = math.cos(phi1)
    
    theta2 = b[1]
    phi2 = b[2]
    x2 = math.cos(theta2)*math.sin(phi2)
    y2 = math.sin(theta2)*math.sin(phi2)
    z2 = math.cos(phi2)   
    
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2))




def genOrdering(a,points):
    
    ordering = []
    dists = []
    tdists = []
    
    for p in points:
        dists.append(dist(a,p))
        tdists.append(dist(a,p))
        
        
    while len(tdists) > 0:
        minD = min(tdists)
        ordering.append(dists.index(minD))
        tdists.remove(minD)
    
    return ordering



maxes = [0] * 26




while True:

    
    #Generate random established points on the sphere.
    num = n    
    
    
    points = []
    
    
    for i in range(num):
        
        
        theta = random.uniform(0.0,3.1415)
        phi = random.uniform(0.0,3.1415*2)       
        
        points.append([r,theta,phi])
        
    
    
    
    
    
    
    
    orderings = []
    
    #Test a lot of random points.
    
    for i in range(numPointsToSim):
        
    
        theta0 = random.uniform(0.0,math.pi)
        phi0 = random.uniform(0.0,math.pi*2)   
        
        
        
        
        point = [1,theta0,phi0]
    
        order = genOrdering(point,points)
    
        if order not in orderings:
            orderings.append(order)

    
        
    
    numOrds = len(orderings)
        
    if maxes[n] < numOrds:
        maxes[n] = numOrds
        print("New max for n = " + str(n) +": " + str(numOrds))
        print(maxes)
        
    
    n = (n + 1) % 26
    
    if n == 0:
        n = n + 3 % 26
    


