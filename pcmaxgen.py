# -*- coding: utf-8 -*-
"""
P||Cmax  instances generator
"""
import random


nazwa =input('type in  name of instance: ')
maxn = int(input('type in maximal task time: '))
nazwa = '{}.txt'.format(nazwa)
f= open(nazwa, 'w')
N_P = 0
N_T = 0
while N_P == 0 or N_T ==0 :
    N_P  = int(input('num of procesors: '))
    N_T = int(input('Num Of Tasks: '))
    if N_P>N_T:
        print ('error, number of tasks must be at least equal to number of procesors, for instances generating allgorithm to work, please reenter data.')
        N_P=0
        N_T=0
        
f.write('{}\n{}\n'.format(N_P, N_T) )

list_of_sums=[]
for i in range(0,N_P): list_of_sums.append(0)
iterator=0
for i in range (0, N_T-N_P):
    l=random.randrange(1,maxn+1,1)
    f.write('{}\n'.format(l))
    list_of_sums[iterator]+=l
    iterator+=1
    iterator = iterator%N_P
max_sum= max(list_of_sums)
max_sum+=random.randrange(1,maxn,1)
for i in list_of_sums:
    f.write('{}\n'.format(max_sum-i))
    
f.write('min T = {}'.format(max_sum))
    
print(max_sum)
f.close()