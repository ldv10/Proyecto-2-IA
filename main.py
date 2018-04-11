# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:09:43 2018

@author: ldv"""

from funciones import *

cant = openFile("test.txt")
#returns total of ham, total of spam, data


#data[0]-> clasificado (depende del porcentaje)

#Gets % , number of total Spam, number of total Ham, array of data
#data = classifier(0.1,cant[0],cant[1],cant[2])
#returns classified, unclassified, cantidad de ham en clasificado y cantidad de spam en clasificado

training = classifier(0.8,cant[0],cant[1],cant[2]) 
cross = classifier(0.1,cant[0],cant[1],training[1])
test1 = classifier(0.1,cant[0],cant[1],cross[1])

dictionaries = dictionary(training[0])
dHam = dictionaries[0]
dSpam = dictionaries[1]

totSpam = training[3]
totHam = training[2] 

totSentences = totSpam + totHam
#P(Spam) o P(Ham)
probHam = totHam/totSentences
probSpam = totSpam/totSentences


y = open("ruebas.txt","r")
test = []
for i in y:
    test.append(i)
    
arch = open("results.txt","w")

for i in test:
    finalSpam = p2(i,"spam","ham",dHam,dSpam,probHam,probSpam)
    finalHam = p2(i,"ham","spam",dHam,dSpam,probHam,probSpam)
    if finalHam > 0.6:
        print("Ham")
        arch.write("ham" + "\t" + i + "\n")
        #arch.write("ste ham")
    else:
        print("Spam")
        arch.write("spam" + "\t" + i + "\n")
        #arch.write("ste spam")