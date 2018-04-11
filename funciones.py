# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 19:02:28 2018

@author: soporte2
"""

#Proyecto 2
#Prueba
import random
#from random import Shuffle
from collections import Counter
        


def openFile(name):
    #returns total of ham and spam and data shuffled
    x = open(name,"r")
    nHam = 0
    nSpam = 0
    data = []
    for i in x:   
        x = lineSeparator(i)
        tipo = x[0]
        if (tipo == "ham"):
            nHam = nHam +  1
        elif (tipo == "spam"):
            nSpam = nSpam + 1   
        data.append(i)
    shuffler(data)
    return nHam, nSpam, data 

def shuffler(data):
    #shuffles data
    x = random.shuffle(data)
    return x

def healer(text):
    #cleans data
    char = "()-,;.?!><[]1234567890\n&$€+-'_:/â=*@#%^+|\"£"
    for c in char:
        text = text.replace(c, "")
    text = text.lower()
    return text

#Gets % , number of total Spam, number of total Ham, array of data
def classifier(per,nHam,nSpam,data):
    #classifies data
    classified = []
    unclassified = []
    unique = set() #Se pone set porque list no tiene el metodo add
    ham = 0
    spam = 0    
    for i in data:
        x = lineSeparator(i)
        tipo = x[0]
        i = healer(i)
        for x in x[1]:
            unique.add(x)
        single = list(unique)
        if tipo == "ham":
            if ham <  (nHam*per):
                classified.append(i)
                ham = ham + 1
        elif tipo == "spam":
            if spam < (nSpam*per):
                classified.append(i)
                spam = spam + 1
        if i not in classified:
                unclassified.append(i)
    return classified, unclassified, ham, spam, single

def lineSeparator(line):
    sh = line.index('\t')
    tipo = line[:sh]
    content = line[sh:]
    content = content.split(" ")
    return tipo, content

#P(X|spam o ham) = (total(x in spam o ham) + k) /(totalPalabra(spam o ham) + k * (palabras unicas))
def p1(word,tipo,k,dicc1,dicc2):
    if tipo == "ham":
        totD = len(dicc1) #total palabras en diccionario
        totX = dicc1[word] #total de palabra en diccionario
    elif tipo == "spam":
        totD = len(dicc2)
        totX = dicc2[word] #total de palabra en diccionario
    prob = (totX + k)/(totD + k*2)
    
    return prob

#P(Spam|mensaje) = 
def p2(sentence,tipo,tipo2,dHam,dSpam,probHam,probSpam):
    a = []
    b = []
    sentence = sentence.split()
    for i in sentence:
        x  = p1(i,tipo,0.1,dHam,dSpam)
        a.append(x)
    nominador = 1
    for num in a:
        nominador = nominador * num #a
    for i in sentence:
        x  = p1(i,tipo2,0.1,dHam,dSpam)
        b.append(x)
    denominador = 1
    for num in b:
        denominador = denominador * num
    nominador = nominador * probHam
    denominador = denominador * probSpam
    return nominador/(nominador + denominador)

            
def dictionary(data):
    dHam = []
    dSpam = []
    ham = []
    spam = []
    for i in data:
        x = lineSeparator(i)
        tipo = x[0]
        if tipo == "ham":
            dHam.append(i)
        if tipo == "spam":
            dSpam.append(i)
    for z in dSpam:
        l = lineSeparator(z)
        for a in l[1]:
            spam.append(a)
    for c in dHam:
        f = lineSeparator(c)
        for b in f[1]:
            ham.append(b)
    spam = Counter(spam)
    ham = Counter(ham)
    return ham, spam
    
    
def optimi(data):
    for i in data:
        finalSpam = p2(i,"spam","ham",dHam,dSpam,probHam,probSpam)
        finalHam = p2(i,"ham","spam",dHam,dSpam,probHam,probSpam)
        if porcentaje > 90:
            return k
    
    
    
    
    
    
    