# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:35:59 2018

@author: ldv
"""
from funciones2 import *
import numpy as np
import matplotlib as mpl

x = open("coordenadas.txt","r")
data = []
data2 = []

for i in x:
    char = "[,]"
    for c in char:
        i = i.replace(c, "")
    line = i.split(' ')
    line[0] = float(line[0])
    line[1] = float(line[1])
    x = ([line[0]],[line[1]])
    data.append(line)   
data = np.asarray(data)

#mpl.pyplot.plot(data[:,0], data[:,1], '.', color='black');
#mpl.pyplot.show()

#Paso 1 ------- inicializacion
numeroK = 2 #Numeros de Kluster
sets = []
pis = pis(numeroK)
for i in range(numeroK):
    x = (sig(),mu(),pis[0,i])
    sets.append(x)


#gaus = gausiano(data[1],3)

