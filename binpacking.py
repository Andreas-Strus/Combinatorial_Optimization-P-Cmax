# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:06:19 2018

@author: Andreas
"""    
from copy import deepcopy
def pack(tasks, num_of_procesors, limit):
    for i in range(0,num_of_procesors):
        #print("\n")
        time = 0
        while (tasks!=[] and (time + tasks[0])<=limit):
            temp=tasks[0]
            time+=temp
            #print('{}'.format(temp))
            tasks.remove(temp)
        
        if (tasks!=[] and time!=limit and not(time+tasks[-1]>limit)):
            act_fit=[[-1],tasks[-1]]
            best_fit=deepcopy(act_fit)
            length = -1*len(tasks)
            first = -1
            second = -2
            third = -3
            doubles=False
            triples=False
            while(first-1>length and time+tasks[first-1]<=limit):
                first-=1
            act_fit = [[first],tasks[first]]
            best_fit = deepcopy(act_fit)
            first=-1
            while((time + act_fit[1])!= limit and not(doubles or triples)):
                if(not(doubles)):
                    if(time+tasks[first]+tasks[second]<=limit):
                        while(second-1>length and tasks[first]+tasks[second-1]+time<=limit):
                            second-=1
                        act_fit = [[first,second],tasks[first]+tasks[second]]
                        if[act_fit[1]>best_fit[1]]:
                            best_fit = deepcopy(act_fit)
                        if(first-1>length):
                            first-=1
                            second = first-1
                    else:
                        first=-1
                        second=-2
                        doubles = True
                elif(not(triples)):
                    if(time+tasks[first]+tasks[second]+tasks[third]<=limit):
                        while(third-1>length and tasks[first]+tasks[second]+tasks[third-1]+time<=limit):
                            third-=1
                        act_fit = [[first,second,third],tasks[first]+tasks[second]+tasks[third]]
                        if(second-1 >length):
                            second-=1
                            third=second-1
                        elif(first-2>length):
                            first-=1
                            second= first-1
                            third= second-1
                        if[act_fit[1]>best_fit[1]]:
                            best_fit = deepcopy(act_fit)
                    else:
                        triples=True
            to_remove=[tasks[j] for j in best_fit[0]]
            for j in to_remove:
                #print('{}'.format(j))
                tasks.remove(j)
                
    if(tasks==[]):
        return True
    else:
        return False
    
def binpacking(tasks, proc):
    task=tasks[:]
    task.sort(reverse = True)
    avg=sum(task)/proc
    limit=int(avg)
    multip=1
    accuracy=0.05
    while(not(pack(task[:],proc, limit))):
        multip+=accuracy
        limit=int(avg*multip)   
    result=limit
    accuracy = accuracy/2
    multip-=accuracy
    while(avg*accuracy>0.5):
        limit=int(avg*multip)
        accuracy = accuracy/2
        if(pack(task[:],proc,limit)):
            multip-=accuracy
            result=limit
        else:
            multip+=accuracy
    return result