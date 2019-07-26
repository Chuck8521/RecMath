# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:04:19 2019

@author: ckuli
"""


import math
import random




def dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def genOrdering(circP):
    
    ordering = []
    dists = []
    tdists = []
    
    for p in points:
        dists.append(dist(circP,p))
        tdists.append(dist(circP,p))
        
        
    while len(tdists) > 0:
        minD = min(tdists)
        ordering.append(dists.index(minD))
        tdists.remove(minD)
    
    return ordering






numPoints = 1500000

RAD = 50.0

n = 5

while True:

    
    #Generate random established points in a box region.
    num = n
    
    #rawPoints = raw_input("Enter your points x,y in a space-separated list: ")
    
    #points = [[2.5614935635339853, 0.22052234976046492], [0.8430424740470159, -2.1244519018107537], [2.78617998617099, 1.4725559638474532], [1.4654636505914906, -1.201047544997071]]
    points = []
    
    for i in range(n):
        
        x = random.uniform(-25.0,25.0)
        y = random.uniform(-25.0,25.0)            
        points.append([x,y])
    
    
    
    
    
    
    
    
         
    #print("------- computing data for " + str(num) + " points ------- " )
    
    
    
    orderings = []
    pointsOrder = []
    
    for i in range(numPoints):

            
            
            
            
        
        x = random.uniform(-RAD,RAD)
        y = random.uniform(-RAD,RAD)
        
        

            
        circP = [x,y]
            
        
        order = genOrdering(circP)
    
        if order not in orderings:
            orderings.append(order)
            pointsOrder.append(circP)
            
    
        
        
        
        
    """if len(orderings) >= 17:
        print(points)
        print(orderings)
        index = orderings.index([2,0,1,3])
        print(pointsOrder[index])
        print(dist(pointsOrder[index],points[0]))
        print(dist(pointsOrder[index],points[1]))
        print(dist(pointsOrder[index],points[2]))
        print(dist(pointsOrder[index],points[3]))
        print(genOrdering(pointsOrder[index]))
    """
        
    print("n = " + str(n) + " yields: " + str(len(orderings)))
    

    #n += 1
    
    
    
