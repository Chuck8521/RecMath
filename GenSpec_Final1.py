# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:41:47 2019

@author: ckuli
"""

import operator as op
from functools import reduce
from copy import deepcopy

from itertools import combinations
from itertools import permutations


#Constants.
MAX = 200
verbose = False
progTrack = False
displayCounts = False
useManualExtra = True
printPercents = True
intersectionThreshold = 1


#Well-established methods ------------


def ncr(n, r):
    
    if n < r:
        return 0
    
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom



def numReg(n, a, b, betaS, alphaS, e, c, d, betaC, alphaC):
    
    
    #Auto-generated constants
    
    alphaPrime = 0
    
    
    for q in alphaC:
        alphaPrime += sum(q)
        
    for q in alphaS:
        for qq in q:
            alphaPrime += sum(qq)
    
    
    
    
    y = len(c)
    p = []
    for i in range(len(a)):
        p.append(len(a[i]))
        
    k = len(p)
    
    
    
    
    
    
    #Current: Linear, cyclic, and e with INDEPENDENT coincidence but no > triple intersections organically or DEPENDENT
    
    
    
    
    
    
    v = ncr(ncr(n,2) - alphaPrime,2) + 1 - 2 * ncr(n,3)
    
    
    #Circle Calc!
    temp1 = 0
    temp2 = 0
    for w in range(y):
        
        temp1 += c[w] * ncr(d[w],3)
        temp2 += c[w] * (ncr(ncr(d[w],2) - sum(alphaC[w]),2) - 1)
        
    v += 2 * temp1
    v -= temp2
    #End Circle Calc!
    
    
    for i in range(k):
        
        t = 0
        q = 0
        
        for j in range(p[i]):
            
            t += a[i][j] * (ncr(b[i][j],2) - sum(alphaS[i][j]))
            q += a[i][j] * ncr(b[i][j],3)
            
        t += e[i]
        
        v -= ncr(t,2)
        v += 2 * q
        
        
        
    
        
        
    
    
    
    #print("Vertices: " + str(v))
    
    
    
    
    
    
    
    
    edges = ncr(n,2) - alphaPrime
    
    for i in range(k):
        
        t = 0
        
        for j in range(p[i]):
                
            t += a[i][j] * (ncr(b[i][j],2) - sum(alphaS[i][j]))
            
        t += e[i]
            
        edges -= t
        
        
        
        
        
    #Circle Calc!
    tmp = 0
    for w in range(y):
        
        tmp += c[w] * (ncr(d[w],2) - sum(alphaC[w]))
        
        
    edges -= tmp
    #End Circle Calc!
    
    
    edges = edges * (ncr(n,2) - alphaPrime - (n - 2))
    
    #End normal line calc.
    
    
    
    
    
    #Circle Calc!
    tmp = 0
    for w in range(y):
        
        tmp += c[w] * (ncr(d[w],2) - sum(alphaC[w]) - betaC[w]) * (1 + ncr(n,2) - alphaPrime - (ncr(d[w],2) - sum(alphaC[w])) + 1 - (n - d[w]))# + alphaC[w]))
        
        for q in range(betaC[w]):
            tmp += (1 + ncr(n,2) - alphaPrime - (ncr(d[w],2) - sum(alphaC[w])) + 1 - (alphaC[w][q] + 1) * (n - d[w]))
        
    edges += tmp
    #End Circle Calc!
    
    
    
    
    for i in range(k):
        
        tot = 0
        
        for j in range(p[i]):
            
            r = 1 + ncr(n,2) - alphaPrime - e[i] - (n - b[i][j])
            
            for q in range(p[i]):
                
                r -= a[i][q] * (ncr(b[i][q],2) - sum(alphaS[i][q]))
            
            tot += (a[i][j] * (ncr(b[i][j],2) - sum(alphaS[i][j])) - betaS[i][j]) * r
            
            
            #Beta Stuff
            
            for q in range(betaS[i][j]):
                
                rrr = (1 + ncr(n,2) -  alphaPrime - e[i] - (alphaS[i][j][q] + 1) * (n - b[i][j]))
            
                
                for qq in range(p[i]):
                
                    rrr -= a[i][qq] * (ncr(b[i][qq],2) - sum(alphaS[i][qq]))
                    
                tot += rrr
            
            
            
        rr =  (1 + ncr(n,2) - alphaPrime - e[i] - (n - 2))
        
        for q in range(p[i]):
            
            rr -= a[i][q] * (ncr(b[i][q],2) - sum(alphaS[i][q]))
        
        tot += e[i] * rr
            
        edges += tot
        
        
            
        
        #Beta stuff
        
        """newR = (1 + ncr(n,2) - alphaPrime - e[i] - (sumBetaS[i] + 1) * (n - 2))
        
        for q in range(p[i]):
            newR -= a[i][q] * (ncr(b[i][q],2) - sumAlphaS[i][q])
            
        edges += sumBetaS[i] * newR"""
    
    
    
    
    
    #print("Edges: " + str(edges))
    
    f = 2 - v + edges
    
    return f
    
    #print("Faces: " + str(f))





#Generates the initial alpha string for the totally linear case.
#Builds up via my algorithm from n = 4 to the wanted n.
#Add 1 to every location past the center, and then add two 1's on the end.
def genNAlpha(nin):    
    
    na= [1]
    
    nn = 4
    
    while nn < nin:
        
        for i in range(((len(na) / 2) + 1), len(na)):
            na[i] += 1
            
        na.append(1)
        na.append(1)
        
        nn += 1    
    
    
    return na






def stripZeroes(a):
    
    ar = []
    
    for i in a:
        if i != 0:
            ar.append(i)
            
    return ar
















#Newer methods. ---------------------



def thisIsValid(config):
    
    #Given a configuration, enforce all of the rules and see if validity holds.
    
    valid = True
    
    for i in range(len(config)):
        
        isLine = True
        
        currentStructure = config[i]
        
        #Go through all subsequent structures and count number of intersections for each.
        
        
        #Keep track of what each intersection is with.
        inters = []
        
        
        
        for j in range(i + 1,len(config)):
            
            
            
            #Count number of intersections.
            intersections = 0
            
            interLine = True
            
            for x in range(len(currentStructure)):
                
                if currentStructure[x] == config[j][x] and config[j][x] != -1 and config[j][x] != 0:
                    
                    #Both are in the same parallel class. This is not valid.
                    return False
                
                elif currentStructure[x] != 0 and config[j][x] != 0:
                    
                    inters.append((config[j][x], x))
                    
                    intersections += 1
                    
                    if currentStructure[x] == -1:
                        isLine = False
                    
                    if config[j][x] == -1:
                        interLine = False
                        
                        

            if intersections > intersectionThreshold:
                return False
            #elif intersections == intersectionThreshold and isLine and interLine:
            #    return False
                
                
        
        #Now we have to check that parallel classes are handled correctly.
        
        for q in range(len(inters)):
            
            pair = inters[q]
            
            parClass = pair[0]
            lineNum = pair[1]
            
            lastParClass = 0
            
            doubleUsed = False
            
            for w in range(q + 1, len(inters)):
                
                nextPair = inters[w]
                
                nextParClass = nextPair[0]
                nextLineNum = nextPair[1]
                
                if parClass == nextParClass and parClass != -1:
                    
                    return False
                    #These // classes are equal.  If line Nums are equal then we can't have any more doubles.
                    """if lineNum == nextLineNum:
                        
                        if doubleUsed:
                            return False
                        else:
                            doubleUsed = True
                            
                    else:
                        
                        if lastParClass == nextParClass and doubleUsed:
                            return False
                        elif lastParClass == nextParClass:
                            doubleUsed = True
                    """
                        
                        
                lastParClass = nextParClass
                            
                            
        
        
                
    return valid






#Return True if a valid one is found, False is no valid one exists.
def tryAllPossibleOfIndex(qonfig, index):
    
    config = qonfig
    
    
    
    if thisIsValid(config):
        return True    
    
    
    
    elif index >= len(config):
        #Base case. Isn't valid.
        return False
        
        
        

    elif index <= 0:
        #First one doesn't matter. If it got this far, then there's no hope.
        #Maybe unneccesarry if I structure the generating method differently?
        return False




    else:
        
        struc = config[index]
    
    
        
        #TODO: Horribly inefficient? AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH IT IS
        allPoss = list(set(permutations(struc,r = len(struc))))
        
        #Converting to set removes the duplicates in the set.
        
        allPossible = []
        
        
        for i in range(len(allPoss)):
            allPossible.append(list(allPoss[i]))
        
        
        
        
        for j in range(len(allPossible)):
            
            
            
            newConfig = config[:index] + [allPossible[j]] + config[index + 1:]

            
            shortConfig = newConfig[:index + 1]
                
            if thisIsValid(shortConfig): 
            
                
                #We progressed the current index by one lexographically. Test for validity.
                if thisIsValid(newConfig):
                    return True
                else:
                    #This isn't valid. Check all possible further indices from this one.
                    
                    #For performance: only actually do this is the config UP TO AND INCLUDING this is valid.
                    
                    return tryAllPossibleOfIndex(newConfig, index + 1)
           
            
        return False







def isValid(a, n):
    
    #(n, a, b, betaS, alphaS, e, c, d, betaC, alphaC)
    #config = [[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [2], [[1,1]]]
    
    #Break config into lines and circles.
    #TODO: Add parallel classes and e. TODO? Assumes all a = 1.

    
    parClasses = []
    circles = []
    
    numParClasses = len(a[4])
    numCircles = len(a[6])
    
    #Make sure neither of these are just 0!
    #For example, if a[6] = [0], we don't want to count it.
    
    if a[4] == [0] and a[0][0] == [0]:
        numParClasses = 0
    
    if a[6] == [0]:
        numCircles = 0
    
    
    #Keep track of total lines so we know how many columns to add to config 2D array.
    numTotalLines = 0
        
    for i in range(numParClasses):
        
        parClass = [a[0][i], a[1][i], a[2][i], a[3][i], a[4][i]]
        
        #print(parClass[4])
        
        numTotalLines += len(parClass[1]) + parClass[4]
        
        parClasses.append(parClass)
        
    for i in range(len(a[6])):
        
        circle = [a[5][i], a[6][i], a[7][i], a[8][i]]
        
        circles.append(circle) 
        
        
    #I now have lines and circles separate.

    #Start adding them into config.
    
    
    numStructs = numTotalLines + numCircles
    
    config = [[0] * n for _ in range(numStructs)]
    
    
    
    
    doLines = False
    index = 0
    parClassNum = 0
    
    #Add structures as default into config.
    #for i in range(len(config)):
    while index < len(config):
        
        if index == numCircles:
            
            doLines = True
            
            
        if doLines:
            
            #We are now looking at adding parallel classes.
            
            parClass = parClasses[parClassNum]
            
            
            for q in range(len(parClass[1])):
                
                
                #This is a line that needs to be added.
                pointsOnLine = parClass[1][q]
            
                defaultC = [0] * n
                
                for j in range(pointsOnLine):
                    defaultC[j] = parClassNum + 1
                    
                
                
                permuts = list(set(combinations(defaultC,r = len(defaultC))))
                
                config[index] = list(permuts[0])
            
            
                #Increment index by number of added structures.
                index += 1    
                
                
            #Now deal with e.
            
            if parClass[4] != 0:
                
                #There is AT LEAST one e to add.
                
                for _ in range(parClass[4]):
                    
                    defaultC = [0] * n
                    
                    for j in range(parClass[4] * 2):
                        
                        #If e cannot be possible:
                        if j == len(defaultC):
                            return False
                        
                        defaultC[j] = parClassNum + 1
                        
                    
                    
                    permuts = list(set(combinations(defaultC,r = len(defaultC))))
                    
                    config[index] = list(permuts[0])
                
                
                    #Increment index by number of added structures.
                    index += 1    
            
            
            #Increment the current parClass.
            parClassNum += 1
            
            
        else:
            
            #We are still adding circles.
            
            circle = circles[index]
            
            pointsOnCircle = circle[1]
            
            
            defaultC = [0] * n
            
            for j in range(pointsOnCircle):
                defaultC[j] = -1
                
                
            
            
            permuts = list(set(combinations(defaultC,r = len(defaultC))))
            
            config[index] = list(permuts[0])
            
            #Circles are always one structure added.
            index += 1
            
            
            
            

    return tryAllPossibleOfIndex(config,1)
        
        
        













        
        

#TODO
#TODO
#TODO




#9 -> 14
#8 -> 10
#7 -> 7
#6 -> 3

#isValid(a,n) is working.

#print(isValid([[[1]], [[3]], [[0]], [[[0]]], [1], [0], [0], [0], [[0]]],5))
#print(isValid([[[0]], [[0]], [[0]], [[[0]]], [0], [1,1,1,1,1,1,1], [4,4,4,4,4,4,4], [0,0,0,0,0,0,0], [[0],[0],[0],[0],[0],[0],[0]]],7))
#print(isValid([[[0]], [[0]], [[0]], [[[0]]], [0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]],9))



#n = 3 does weird things because of beta formula. Treat it as an edge case.
n = 4


#Store all structures that use n points in the pointStrucs[n].
pointStrucs = [[] for i in range(MAX + 1)]

pointStrucsC = [[] for i in range(MAX + 1)]

pointStrucsE = [[] for i in range(MAX + 1)]

pointCombos = [[] for i in range(MAX + 1)]

#Store all past configurations here, in the total toolbox, as it were.
configs = [[[[1]], [[3]], [[0]], [[[0]]], [0], [0], [0], [0], [[0]]]]#Max, 1/3/0

#Append the only 3 point structure.
pointStrucs[3].append([[[1]], [[3]], [[0]], [[[0]]], [0], [0], [0], [0], [[0]]])

linearConfigs = []

while n < MAX:
    
    #Store all seen numbers on the spectrum here.
    seenReg = []


    if n == 5 and useManualExtra:
        
        extraConfig = [[[1],[1]], [[3],[3]], [[0],[0]], [[[0]],[[0]]], [0,0], [1], [4], [0], [[0]]]
        configs.append(extraConfig)
        extraConfig = [[[1],[1]], [[3],[3]], [[0],[0]], [[[0]],[[0]]], [0,0], [1], [4], [1], [[1]]]
        configs.append(extraConfig)
        extraConfig = [[[1],[1]], [[3],[3]], [[0],[0]], [[[0]],[[0]]], [0,0], [1], [4], [2], [[1,1]]]
        configs.append(extraConfig)
        
        #These just need 2 intersection threshold.
        extraConfig = [[[1]], [[3]], [[0]], [[[0]]], [0], [1], [4], [2], [[1,1]]]
        configs.append(extraConfig)
        extraConfig = [[[1]], [[3]], [[0]], [[[0]]], [0], [1], [4], [1], [[1]]]
        configs.append(extraConfig)
        extraConfig = [[[1]], [[3]], [[0]], [[[0]]], [0], [1], [4], [0], [[0]]]
        configs.append(extraConfig)
    


    # ADD LINEAR COMBOS --------------------
    
    
    #TODO: Idea list for optimization: keep track of what things can combo with each to lower combos tried.
    #Less computation on the recursive hell method, the better.
    
    
    qonfigs = deepcopy(configs)
    
    
    ind = 0
    
    #Add linear substructure into a NEW parallel class.
    for a in qonfigs:
        
        if progTrack and False:
            print("new a: " + str(ind) + "/" + str(len(qonfigs)))
            ind += 1
        
        newCon = deepcopy(a)
        
        stillValid = True
        
        #Search for a linear structure to be in a new parallel class.
        for b in range(3,len(pointStrucs)):
            
            #stillValid should be false whenever there is a config that is 
            #   invalid in b. No 5 will work if 4 can't, etc.
            if stillValid:
            
                options = pointStrucs[b]
                
    
                for option in options:
                    #Combo option and newCon.
                    
                    newConfig = deepcopy(newCon)
                    
                    #(a, b, betaS, alphaS, e, c, d, betaC, alphaC)
                    #configs.append([[[0]], [[0]], [[0]], [[[0]]], [n / 2], [0], [0], [0], [[0]]])
                    
                    
                    if newConfig[0] == [[0]]:
                        newConfig[0] = option[0]
                        newConfig[1] = option[1]
                        newConfig[2] = option[2]
                        newConfig[3] = option[3]
                        newConfig[4] = option[4]
                    else:
                        newConfig[0].append(option[0][0])
                        newConfig[1].append(option[1][0])
                        newConfig[2].append(option[2][0])
                        newConfig[3].append(option[3][0])
                        newConfig[4].append(option[4][0])
                    
                    
                    #Add to pointCombos[n] when done for further use in future combos..?
    
                    #Add to configs if valid.
                    
                    validity = isValid(newConfig, n)
                    
                    if newConfig not in qonfigs and validity:
                        configs.append(newConfig)
                        qonfigs.append(newConfig)
                    
                    
                        a1 = newConfig[0]
                        b1 = newConfig[1]
                        betaS1 = newConfig[2]
                        alphaS1 = newConfig[3]
                        e1 = newConfig[4]
                        c1 = newConfig[5]
                        d1 = newConfig[6]
                        betaC1 = newConfig[7]
                        alphaC1 = newConfig[8]
                    
                        reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1)                   
                        
                        if verbose:
                            print("Combo region: " + str(reg))
                            print(newConfig)
                    
                    elif not validity:
                         stillValid = False
                         break
                        
                        
                        
                        #Because it's valid, we should go through and make sure we can't add any more.
    
                    #Now, what if we have option added to newConfig in a new // class.
                        
                    #(a, b, betaS, alphaS, e, c, d, betaC, alphaC)
                    
                    
                    if newCon[0] == [[0]]:
                        #There are no // classes to add this novelly to. Exit.
                        continue
                    
                    else:
                        
                        
                        for parClass in range(len(a[0])):
                            
                            newConfig2 = deepcopy(newCon)
                            
                            newConfig2[0][parClass].append(option[0][0][0])
                            newConfig2[1][parClass].append(option[1][0][0])
                            newConfig2[2][parClass].append(option[2][0][0])
                            newConfig2[3][parClass].append(option[3][0][0])
                            
                            #newConfig2 is ready for testing.
                            
                            if newConfig2 not in configs and isValid(newConfig2, n):
                                configs.append(newConfig2)
                                qonfigs.append(newConfig2)
                            
                            
                                a1 = newConfig2[0]
                                b1 = newConfig2[1]
                                betaS1 = newConfig2[2]
                                alphaS1 = newConfig2[3]
                                e1 = newConfig2[4]
                                c1 = newConfig2[5]
                                d1 = newConfig2[6]
                                betaC1 = newConfig2[7]
                                alphaC1 = newConfig2[8]
                            
                                reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1)                   
                                
                                if verbose:
                                    print("Linear combo region same // class: " + str(reg))
                                    print(newConfig2)

    
    
    # ADD LINEAR COMBOS END ----------------
    
    
    



    if progTrack:
        print("done with lin combos")




    


    #ADD INDUCED PARALLEL COMBOS -----------
    
    
    qonfigs = deepcopy(configs)
    
    
    
    #Add induced parallel NEW parallel class.
    for a in qonfigs:
        
        
        
        newCon = deepcopy(a)
        
        
        
        
        #SPECIAL CASE: e = 1.
        #This can be added into any non-empty parallel class in a.
        
        if newCon[0] == [[0]]:
            #There are no // classes to add this novelly to. Exit.
            pass
        
        else:
            
            
            
            for parClass in range(len(a[4])):
                
                newConfig2 = deepcopy(newCon)

                
                    
                newConfig2[4][parClass] += 1
                

                #newConfig2 is ready for testing.
                
                if newConfig2 not in configs and isValid(newConfig2, n):
                    configs.append(newConfig2)
                    qonfigs.append(newConfig2)
                
                
                    a1 = newConfig2[0]
                    b1 = newConfig2[1]
                    betaS1 = newConfig2[2]
                    alphaS1 = newConfig2[3]
                    e1 = newConfig2[4]
                    c1 = newConfig2[5]
                    d1 = newConfig2[6]
                    betaC1 = newConfig2[7]
                    alphaC1 = newConfig2[8]
                
                    reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1)                   
                    
                    if verbose:
                        print("E combo region same // class, e = 1: " + str(reg))
                        print(newConfig2)
        
        
        
        
        
        stillValid = True
        
        #Search for a linear structure to be in a new/old parallel class.
        for b in range(4,len(pointStrucsE),2):
            
            if stillValid:
                
                options = pointStrucsE[b]
                
    
                for option in options:
                    #Combo option and newCon.
                    
                    newConfig = deepcopy(newCon)
                    
                    #(a, b, betaS, alphaS, e, c, d, betaC, alphaC)
                    #configs.append([[[0]], [[0]], [[0]], [[[0]]], [n / 2], [0], [0], [0], [[0]]])
                    
                    
                    if newConfig[0] == [[0]]:
                        newConfig[0] = option[0]
                        newConfig[1] = option[1]
                        newConfig[2] = option[2]
                        newConfig[3] = option[3]
                        newConfig[4] = option[4]
                    else:
                        newConfig[0].append(option[0][0])
                        newConfig[1].append(option[1][0])
                        newConfig[2].append(option[2][0])
                        newConfig[3].append(option[3][0])
                        newConfig[4].append(option[4][0])
                    
                    
                    #Add to pointCombos[n] when done for further use in future combos..?
    
                    #Add to configs if valid.
                    
                    validity = isValid(newConfig, n)
                    
                    if newConfig not in configs and validity:
                        configs.append(newConfig)
                        qonfigs.append(newConfig)
                    
                    
                        a1 = newConfig[0]
                        b1 = newConfig[1]
                        betaS1 = newConfig[2]
                        alphaS1 = newConfig[3]
                        e1 = newConfig[4]
                        c1 = newConfig[5]
                        d1 = newConfig[6]
                        betaC1 = newConfig[7]
                        alphaC1 = newConfig[8]
                    
                        reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1)                   
                        
                        if verbose:
                            print("E combo region: " + str(reg))
                            print(newConfig)                   
                        
                        
                        
                        #Because it's valid, we should go through and make sure we can't add any more.
                        #TODO: Make that work.
                        
                    elif not validity:
                        stillValid = False
                        break
                        
                        
                        
                    #Now, what if we have option added to newConfig in a new // class.
                    
                    #(a, b, betaS, alphaS, e, c, d, betaC, alphaC)
                    
                    
                    if newCon[0] == [[0]]:
                        #There are no // classes to add this novelly to. Exit.
                        continue
                    
                    else:
                        
                        
                        for parClass in range(len(a[0])):
                            
                            newConfig2 = deepcopy(newCon)
                            
                            #print(newConfig2)
                            #print(option)
                        
                            newConfig2[4][parClass] += option[4][0]
                            
                            #newConfig2 is ready for testing.
                            
                            if newConfig2 not in configs and isValid(newConfig2, n):
                                configs.append(newConfig2)
                                qonfigs.append(newConfig2)
                            
                            
                                a1 = newConfig2[0]
                                b1 = newConfig2[1]
                                betaS1 = newConfig2[2]
                                alphaS1 = newConfig2[3]
                                e1 = newConfig2[4]
                                c1 = newConfig2[5]
                                d1 = newConfig2[6]
                                betaC1 = newConfig2[7]
                                alphaC1 = newConfig2[8]
                            
                                reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1)                   
                                
                                if verbose:
                                    print("E combo region same // class: " + str(reg))
                                    print(newConfig2)
                                
                                
                                
                                
                                
                    
                    
                    
            
    
    
    
    
    
    
    
    #ADD INDUCED PARALLEL COMBOS END -------



    





    

    #ADD CYCLIC COMBOS ----------------------------
    
    
    
    qonfigs = deepcopy(configs)
    
    
    for a in qonfigs:
        
        
        
        newCon = deepcopy(a)
        
        stillValid = True
       
        
        #Search for a linear structure to be in a new parallel class.
        for b in range(4,len(pointStrucsC)):
            
            if stillValid:
                
                options = pointStrucsC[b]
                
    
                for option in options:
                    #Combo option and newCon.
                    
                    newConfig = deepcopy(newCon)
                    
                    #(a, b, betaS, alphaS, e, c, d, betaC, alphaC)
                    #configs.append([[[0]], [[0]], [[0]], [[[0]]], [n / 2], [0], [0], [0], [[0]]])
                    
                    
                    if newConfig[5] == [0]:
                        newConfig[5] = option[5]
                        newConfig[6] = option[6]
                        newConfig[7] = option[7]
                        newConfig[8] = option[8]
                    else:
                        newConfig[5].append(option[5][0])
                        newConfig[6].append(option[6][0])
                        newConfig[7].append(option[7][0])
                        newConfig[8].append(option[8][0])
                    
                    
                    #Add to pointCombos[n] when done for further use in future combos..?
    
                    #Add to configs if valid.
                    
                    validity = isValid(newConfig, n)
                    
                    if newConfig not in configs and validity:
                        configs.append(newConfig)
                        qonfigs.append(newConfig)
                    
                    
                        a1 = newConfig[0]
                        b1 = newConfig[1]
                        betaS1 = newConfig[2]
                        alphaS1 = newConfig[3]
                        e1 = newConfig[4]
                        c1 = newConfig[5]
                        d1 = newConfig[6]
                        betaC1 = newConfig[7]
                        alphaC1 = newConfig[8]
                    
                        reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1) 
                        
                        if verbose:
                            print("Cyclic combo region: " + str(reg))
                            print(newConfig)
                        
                        
                    elif not validity:
                        stillValid = False
                        
        
    
    
    
    
    
    
    
    
    
    #ADD CYCLIC COMBOS END ------------------------
    
    
    
    
    
    
    if progTrack:
        print("done with cyc combos")
    
    
    
    
    
    #Now bind all n points in one structure.
    
    
    
    
    
    
    #LINEAR CASE ---------------------------------------------
    
    #Generate (new for this n) linear configs.
    nB = [n]
    nBeta = [(2 * n) - 7]
    
    #Generate the proper beginning nAlpha for this n.
    nAlpha = genNAlpha(n)
        
    newConf = [[[1]], [nB], [nBeta], [[nAlpha]], [0], [0], [0], [0], [[0]]]
    
    end = 2 * n - 8
    nextToSubtract = (2 * n - 7) / 2
       
    while nBeta[0] != 0:
        
        configs.append(deepcopy(newConf))
        pointStrucs[n].append(deepcopy(newConf))
        
        #Modify nBeta and nAlpha in the needed ways to decrease lexographically.        
        if nextToSubtract == end + 1:
            #Uh oh. We need to modify, because the last two are now zeroes.
            end -= 2
            nextToSubtract = (end + 1) / 2
        
        nAlpha[nextToSubtract] -= 1
        if nAlpha[nextToSubtract] == 0:
            nBeta[0] -= 1
        nextToSubtract += 1
        
        #Strip zeroes from the nAlpha array before using.
        nnAlpha = stripZeroes(nAlpha)
        
        newConf = [[[1]], [nB], [nBeta], [[nnAlpha]], [0], [0], [0], [0], [[0]]]
        
               

    #nBeta = 0. Add final new linear config.
    newConf = [[[1]], [nB], [[0]], [[[0]]], [0], [0], [0], [0], [[0]]]
    configs.append(deepcopy(newConf))
    pointStrucs[n].append(deepcopy(newConf))
    
    

    


    #LINEAR CASE END --------------------------






    if progTrack:
        print("done with lin case")








    #CYCLIC CASE ------------------------------
    
    #n = 4 is edge case
    
    if n >= 5:
        d = n
        
        #Generate special cyclic configs, from the d-gon to the 2d-6-gon, then add the two special, and then all the linear repeats.
        
        weirdPres = 0 #Weirdly preserved index, where there is no subtraction by 1.
        
        allArs = []
        
        for i in range(d, 2 * d - 6 + 1):
            
            
            beta = i
            numToAdd = d - 3
            start = 0
            ar = [0] * beta
            
            for j in range(0, d - 2):
                
                place = start
                
                for q in range(0, numToAdd):
                    
                    ar[place] += 1
                    place  = (place + 1) % beta
                    
                if weirdPres != j:
                    numToAdd -= 1
                    
                start = (start + 2) % beta
            
            allArs.append(ar)
            
            weirdPres += 1
            
            
        linMax = genNAlpha(d)
        linMax1 = deepcopy(linMax)
        linMax1.append(1)
        linMax2 = deepcopy(linMax1)
        linMax2.append(1)
        
        allArs.append(linMax2)
        allArs.append(linMax1)
        
        
        for a in allArs:
            configs.append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [d], [len(a)], [a]])
            pointStrucsC[d].append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [d], [len(a)], [a]])
            
            
            
            
            
            
        #Now, all of the special cyclic cases are added to our configuration databases.
        
        
        #Reuse of code to decrease the linear alpha count in the same way. Should probably be a function.
        
        nBeta = (2 * d) - 7
        nAlpha = deepcopy(linMax)
        
        #Generate the proper beginning for this "linear" case.            
        newConf = [[[0]], [[0]], [[0]], [[[0]]], [0], [1], [d], [nBeta], [nAlpha]]
        
        end = 2 * d - 8
        nextToSubtract = (2 * d - 7) / 2
           
        while nBeta != 0:
            
            configs.append(deepcopy(newConf))
            pointStrucsC[d].append(deepcopy(newConf))
            allArs.append(deepcopy(newConf[8][0]))#debug
            
            #Modify nBeta and nAlpha in the needed ways to decrease lexographically.        
            if nextToSubtract == end + 1:
                #Uh oh. We need to modify, because the last two are now zeroes.
                end -= 2
                nextToSubtract = (end + 1) / 2
            
            nAlpha[nextToSubtract] -= 1
            if nAlpha[nextToSubtract] == 0:
                nBeta -= 1
            nextToSubtract += 1
            
            #Strip zeroes from the nAlpha array before using.
            nnAlpha = stripZeroes(nAlpha)
            
            newConf = [[[0]], [[0]], [[0]], [[[0]]], [0], [1], [d], [nBeta], [nnAlpha]]
            
                   
    
        #nBeta = 0. Add final new "linear" config.
        newConf = [[[0]], [[0]], [[0]], [[[0]]], [0], [1], [d], [0],[[0]]]
        configs.append(deepcopy(newConf))
        pointStrucsC[n].append(deepcopy(newConf))
        allArs.append(deepcopy(newConf[8][0]))#debug
            
        
        
        
        
        
        
        #print(allArs) #debug
            
        
        #(n, a, b, betaS, alphaS, e, c, d, betaC, alphaC)
        
        
        
        
        
        
    else:
        
        #n = 4
        #(n, a, b, betaS, alphaS, e, c, d, betaC, alphaC)
        configs.append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [2], [[1,1]]])
        configs.append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [1], [[1]]])
        configs.append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [0], [[0]]])
        
        pointStrucsC[4].append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [2], [[1,1]]])
        pointStrucsC[4].append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [1], [[1]]])
        pointStrucsC[4].append([[[0]], [[0]], [[0]], [[[0]]], [0], [1], [4], [0], [[0]]])
    
    
    
    #CYCLIC CASE END --------------------------




    if progTrack:
        print("done with cyc combos")








    #INDUCED PARALLELS ------------------------
    
    
    #2 points implies 1 more induced parallel (if nothing else in config, like here).
    
    if n % 2 == 0:
        #n is even. This adds a new induced parallel only possibility.
        #(n, a, b, betaS, alphaS, e, c, d, betaC, alphaC)
        configs.append([[[0]], [[0]], [[0]], [[[0]]], [n / 2], [0], [0], [0], [[0]]])
        pointStrucsE[n].append([[[0]], [[0]], [[0]], [[[0]]], [n / 2], [0], [0], [0], [[0]]])
        
    
    
    
    #INDUCED PARALLELS END --------------------



    if progTrack:
        print("done with e")

    
    
    





    #See what region counts are generated.
    
    for config in configs:    
        
        a1 = config[0]
        b1 = config[1]
        betaS1 = config[2]
        alphaS1 = config[3]
        e1 = config[4]
        c1 = config[5]
        d1 = config[6]
        betaC1 = config[7]
        alphaC1 = config[8]
    
        reg = numReg(n, a1, b1, betaS1, alphaS1, e1, c1, d1, betaC1, alphaC1)
        
        if verbose:
            print(config)
            print(reg)
        
        if reg not in seenReg:
            seenReg.append(reg)



    extraReg = numReg(n, [[0]], [[0]], [[0]], [[[0]]], [0], [0], [0], [0], [[0]])
    
    seenReg.append(extraReg)




    #Print all counts.
    print("n = " + str(n) + ": ")
    
    seenReg.sort()
    
    if displayCounts:
        for uh in range(len(seenReg)):
            print(str(seenReg[uh]))
    
    
    out = ""
    
    seen = 0.0
    total = 0.0
    
    for i in range((2 * n) - 2, int((1.0 / 24.0) * (24.0 - 14.0 * n + 21.0 * n**2 - 10.0 * n**3 + 3.0 * n**4) + 1.0)):
        total += 1.0
        if i in seenReg:
            #out += u"\u25A0"
            out += "1"
            seen += 1.0
        else:
            #out += u"\u25A1"
            out += "0"
    
    print(out)
    if printPercents:
        print(str(seen / total))
    
    
 
    
    
    n += 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
