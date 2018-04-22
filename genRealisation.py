# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:57:51 2018

@author: Andreas
"""
import copy
#import random
def find_half(procesor, delta=0):
    suma=0
    index=0
    while(suma<(procesor[1]-delta)/2):
        suma+=procesor[0][index]
        index+=1
    return index
def genetic2(tasks, proc):
    procesors = []
    tasks.sort(reverse = True)
    for i in range(0,proc):
        procesors.append([[],0])
    for i in tasks:
        ind = procesors.index(min(procesors, key= lambda x: x[1]))
        procesors[ind][0].append(i)
        procesors[ind][1]+=i
    counter = int((proc/4)+5)
    best = copy.deepcopy(max(procesors, key = lambda x: x[1]))
    while counter>0:
        counter-=1
#        random.shuffle(procesors)
        procesors.sort(key = lambda x: x[1], reverse = True)
        for i in range(1,int(proc/2)):
            delta = (procesors[i-1][1] -procesors[-1*i][1])
            indminhalf = find_half(procesors[-1*i])
            temp1 = procesors[-1*i][0][indminhalf:]
            indmaxhalf = find_half(procesors[i-1],delta)
            temp2 = procesors[i-1][0][indmaxhalf:]
            procesors[-1*i][0]=procesors[-1*i][0][:indminhalf]+temp2
            procesors[i-1][0]=procesors[i-1][0][:indmaxhalf]+temp1
            procesors[-1*i][1]=sum(procesors[-1*i][0])
            procesors[i-1][1]=sum(procesors[i-1][0])
        result = max(procesors, key = lambda x: x[1])
        if result[1]<best[1]:
            best = copy.deepcopy(max(procesors, key = lambda x: x[1]))
            counter = int((proc/4)+5)
    return best[1]

def genetic3(tasks, proc):
    procesors = []
    tasks.sort(reverse = True)
    for i in range(0,proc):
        procesors.append([[],0])
    for i in tasks:
        ind = procesors.index(min(procesors, key= lambda x: x[1]))
        procesors[ind][0].append(i)
        procesors[ind][1]+=i
    counter = int((proc/4)+5)
    best = copy.deepcopy(max(procesors, key = lambda x: x[1]))
    while counter>0:
        counter-=1
#        random.shuffle(procesors)
        procesors.sort(key = lambda x: x[1], reverse = True)
        for i in range(1,int(proc/2)):
            delta = (procesors[i-1][1] -procesors[-1*i][1])
            indminmin = procesors[-1*i][0].index(min(procesors[-1*i][0]))
            temp1 = procesors[-1*i][0][indminmin]
            indsetmax = procesors[i-1][0].index(min(procesors[i-1][0], key = lambda x: abs(x-temp1-(delta/2))))
            temp2 = procesors[i-1][0][indsetmax]
            procesors[-1*i][0][indminmin]=temp2
            procesors[i-1][0][indsetmax]=temp1
            procesors[-1*i][1]+=(temp2-temp1)
            procesors[i-1][1]+=(temp1-temp2)
        result = max(procesors, key = lambda x: x[1])
        if result[1]<best[1]:
            best = copy.deepcopy(max(procesors, key = lambda x: x[1]))
            counter = int((proc/4)+5)
    return best[1]

def genetic4(tasks, proc):
    procesors = []
    tasks.sort(reverse = True)
    for i in range(0,proc):
        procesors.append([[0]*int(proc/4),0])
    for i in tasks:
        ind = procesors.index(min(procesors, key= lambda x: x[1]))
        procesors[ind][0].append(i)
        procesors[ind][1]+=i
    counter = int((proc/4)+5)
    best = max(procesors, key = lambda x: x[1])[1]
    while counter>0:
        counter-=1
#        random.shuffle(procesors)
        procesors.sort(key = lambda x: x[1], reverse = True)
        for i in range(1,int(proc/2)):
            delta = (procesors[i-1][1] -procesors[-1*i][1])
            indminmin = procesors[-1*i][0].index(min(procesors[-1*i][0], key = lambda x : x if x!=0 else float('inf')))
            temp1 = procesors[-1*i][0][indminmin]
            indsetmax = procesors[i-1][0].index(min(procesors[i-1][0], key = lambda x: abs(x-temp1-(delta/2))))
            temp2 = procesors[i-1][0][indsetmax]
            procesors[-1*i][0][indminmin]=temp2
            procesors[i-1][0][indsetmax]=temp1
            procesors[-1*i][1]+=(temp2-temp1)
            procesors[i-1][1]+=(temp1-temp2)
        result = max(procesors, key = lambda x: x[1])
        if result[1]<best:
            best = max(procesors, key = lambda x: x[1])[1]
            counter = int((proc/4)+5)
    return best