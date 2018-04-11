# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:24:08 2018

@author: ldv
"""
import random as ran
import numpy as np
import math
import mpmath


   
        
def sig():
    det = 0
    while(det == 0):
        #x = ran.random()
        #x = round(ran.uniform(-5,5),1)
        x = ran.randint(-5,5)
        y = ran.randint(-5,5)
        #x = ran.randint(0,9)
        #y = ran.randint(0,9)
        #sigma = np.array([[round(ran.uniform(-5,5),1),0],[0,round(ran.uniform(-5,5),1)]])
#        sigma = np.array([[0,round(ran.uniform(-5,5),1)],[round(ran.uniform(-5,5),1),0]])
        sigma = np.array([[0,x],[y,0]])
        
        #sigma = np.array([[x,0],[0,y]])
        det = np.linalg.det(sigma)
    #mu = ([ran.randint(-5,5),ran.randint(-5,5)])
    return sigma

def mu():
     #mu = ([ran.randint(-5,5),ran.randint(-5,5)])
     mu = ([ran.random(),ran.random()])
     return mu
    

def pis(klosters):
    pi = []
    pi = np.random.dirichlet(np.ones(klosters), size = 1)
    return pi
    

def mul(sigma,mu,punto,pi):
    n = 2
    det = np.linalg.det(sigma)
    mul1 = ((2 * math.pi)**(-n/2)) * (abs(det) ** (-1/2))
    y = np.subtract(punto,mu) #x - mu ->
    trans = np.transpose(y) #^T
    inver = np.linalg.inv(sigma) #sigma ^-1
    p3 = trans @ inver @ y
    mul2 = (-0.5) * p3
    fin = pi *(mul1 * (mpmath.e ** mul2))
    fin = float(fin)
    return fin 

def notNormal(data,sets):
    probs = []
    for i in range(len(data)):
    #for i in range(3):
        r = 0
        for x in range (len(sets)):
        #for x in range (2):
            ex = mul(sets[x][0],sets[x][1],data[i],sets[x][2])
            r = r + ex
        for x in range (len(sets)):
            ex1 = ex/r
            probs.append(ex1)
    #return probs
    #Updatea pi, mu y sigma
    for i in range(len(sets)):
        
        sum1 = 0
        for x in range(len(data)):
            sum1 = sum1 + probs[x + 2]
        sum1 = sum1 + probs[i]
            
        piN =  sum1/len(data)
        
        sum2 = 0
        for x in range(len(data)):
            sum2 = sum2 + probs[x+2] * data[x]
        sum2 = sum2 + probs[i]
        
        muN = sum2/sum1
        
        sum3 = 0
        for x in range(len(data)):
            print("Mu: ",sets[i][1])
            print("Punto: ",data[x])
            sum3 = sum3 + (probs[x+2] * (data[x] - sets[i][1] ) * np.transpose((data[x] - sets[i][1])))
        sigN = sum3/sum1
        
    return sigN
 
    
