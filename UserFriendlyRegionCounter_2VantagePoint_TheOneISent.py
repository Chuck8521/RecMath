# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:04:19 2019

@author: ckuli
"""


import math
import random



def isclose(a,b,sig_fig=5):
    return (a==b or int(a*10**sig_fig) == int(b*10**sig_fig))

def dist(a,b):
    return math.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))

def genOrdering(a,b):
    
    ordering = []
    dists = []
    tdists = []
    
    for p in points:
        
        d1 = dist(a,p)
        d2 = dist(b,p)
        
        dt = (d1 + d2) / 2
        
        
        dists.append(dt)
        tdists.append(dt)
        
        
    while len(tdists) > 0:
        minD = min(tdists)
        ordering.append(dists.index(minD))
        tdists.remove(minD)
    
    return ordering



    
    
    


numPoints = 1000000

level = raw_input("Level of precision (l, m, h, vh): ")

if level == "l":
    numPoints = 200000
elif level == "m":
    numPoints = 500000
elif level == "vh":
    numPoints = 10000000
else:
    numPoints = 2000000

n = input("Number of points in configuration: ")

cMax = 0









    
#Generate random established points in a box region.
num = n


rawPoints = raw_input("Enter your points x,y in a space-separated list: ")
    
points = []

rPoints = rawPoints.split()

for r in rPoints:
    #print(r)
    rr = r.split(",")
    #print(rr[0])
    #print(rr[1])
    x = float(rr[0])
    y = float(rr[1])
    points.append([x,y])





print("------- computing data for " + str(n) + " points ------- " )

while True:


    
    
    
        
    
    orderings = []
            
        
    itr = 0
    while itr < numPoints:

        v1x = random.uniform(-50.0,50.0)
        v1y = random.uniform(-50.0,50.0)
        
        v2x = random.uniform(-50.0,50.0)
        v2y = random.uniform(-50.0,50.0)
        
        p1 = [v1x,v1y]
        p2 = [v2x,v2y]
        
        skip = False
        
        for point in points:
            if isclose(v1x,point[0]):
                skip = True
                #print("hi")
            elif isclose(v1y, point[1]):
                skip = True
                #print("hey")
            elif isclose(v2x,point[0]):
                skip = True
                #print("hiy")
            elif isclose(v2y, point[1]):
                skip = True
                #print("heyy")
    
    
        if not skip:
    
            order = genOrdering(p1,p2)
        
            if order not in orderings:
                orderings.append(order)
        
        itr += 1
    
        
        
    #if len(orderings) > cMax:
    print("Num orderings: " + str(len(orderings)))
    #    cMax = len(orderings)
    #    print(points)
    
    
    
