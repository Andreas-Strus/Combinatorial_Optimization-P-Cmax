# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:08:12 2018

@author: Andreas
"""
import random
from set_finder import set_finder 
from genRealisation import genetic2
from genRealisation import genetic3
from genRealisation import genetic4
from binpacking import binpacking


def alg_chooser (alg, task=[], proc=0):
    
    switcher = {
                1: greedy,
                2: genetic,
                3: genetic2,
                4: genetic3,
                5: genetic4,
                6: binpacking
                }
    
    if (proc!=0):
         return switcher.get(alg,"error: I don't know this algorithm, sorry")(task,proc)
    else:
        return (alg not in switcher)
def assign(tasks, proc):
    sums=[]
    for i in range(0,proc): sums.append(0) #crearion of list which items represent every procesor
    for i in tasks: 
        sums[sums.index(min(sums))]+=i
        #simple assighning of tasks (longest to shortest) to first free procesor   
    return max(sums)
def greedy(tasks, proc):
    #function executing greedy algoritm on a list of tasks and number of procesors
    # tasks - list of tasks
    # proc - number of procesors in specyfic instance of P||Cmax Problem.
    temp_task = tasks[:] # makeing copy of list
    temp_task.sort(reverse = True) #sorting of list
    return assign(temp_task, proc)
    

def genetic(tasks, proc):
    Generation = []
    Newlist=tasks[0:len(tasks)]
#    temp = tasks[0:len(tasks)]
#    temp.sort(reverse=True)
#    Generation.append([temp,0])
    
    for i in range(0,20):
        random.shuffle(Newlist)
        Generation.append([Newlist[0:len(Newlist)], 0])
    for i in Generation: 
        i[1] = assign(i[0], proc)
    counter = 100
    Generation.sort(key = lambda x: x[1])
    best= Generation[0][:]
    while(counter > 0):
        counter-=1
        nonstatic=[]
        for i in range(0, len(Generation[0][0])):
            if not(Generation[0][0][i]==Generation[1][0][i]):
                nonstatic.append(i)
        for i in range(15,11):
            iterator=0
            random.shuffle(nonstatic)
            for j in range(0,len(Generation[0][0])):
                if j in nonstatic:
                    Generation[i][0][j] = Generation[0][nonstatic[iterator]]
                    iterator+=1
                else:
                    Generation[i][0][j]=Generation[0][0][j]
            Generation[i][1] = 0
        for i in range(19,15):
            random.shuffle(Generation[i][0])
            Generation[i][1] = 0
        for i in range(11,5):
            Generation[i][0] = set_finder(Generation[i-6][0][0:len(Generation[0][0])])
        for i in range(5,-1,-1):
            max_mut=int(len(tasks)/20)
#            mut=[]
#            if (max_mut<3): mut = mut +[1,2]
#            else: mut= mut + list(range( 1,random.randint(1,max_mut)))
            for j in range(1,random.randint(1,max_mut)):
                rand1= random.randrange(0,len(Generation[0][0]))
                rand2=random.randrange(0,len(Generation[0][0]))
                while (rand2==rand1): rand2=random.randrange(0,len(Generation[0][0]))
                temp=Generation[i][0][rand1]
                Generation[i][0][rand1]=Generation[i][0][rand2]
                Generation[i][0][rand2]=temp
        for i in Generation: 
            i[1] = assign(i[0], proc)
        Generation.sort(key = lambda x: x[1])
        if (Generation[0][1]< best[1]):
            counter = 100
            best = Generation[0][0:2]
    return best[1]
              
        
        
    

def read_instance(f):
    num_of_procesors = int(f.readline().split()[0])
    num_of_tasks = int(f.readline().split()[0])
    list_of_tasks=[]
    for i in range(0,num_of_tasks):
        list_of_tasks.append(int(f.readline().split()[0]))
    return num_of_procesors, num_of_tasks, list_of_tasks


def main (*args, **kwargs):
    if(input("""Hello, lets start of with question, will your instances prowide optymal solution? (y/n) """)=='y'):
        optymal_present = True
        
    else: optymal_present = False
    list_of_instances = input("""Now lets start, provide me with paths of the instances (separated by blanck spaces only) """).split()
    if(input("""Do you wish to use all algorithms implemented? (y/n) """)=='y'):
        use_all = True
        algs = [1,2,3,4,5,6]
    else: use_all = False
    if not(use_all):
        alg = 0
        while(alg_chooser(alg)): alg = int(input("""I, think it's time then for you to choose an algorithm you want me to use to solve this problem.\n Type in one of numbers from the list bellow:\n1:\tGreedy\n2:\tGenetic\n3:\tGenetic2\n4:\tGenetic3\n5:\tGenetic4\n6:\tbinpacking\n"""))
        algs = [alg]
    if(input("""do you wish to save results? (y/n) """)=='y'):
        to_file = True
        
    else: to_file = False    
    for i in list_of_instances:
        f=open(i,'r')
        num_of_proc, num_of_tasks, list_of_tasks = read_instance(f)
        if to_file:
            results = open('results.txt', 'a')
            for alg in algs:
                results.write("{}\t{}\t{}".format(alg, i, alg_chooser(alg, list_of_tasks, num_of_proc)))
                if optymal_present :
                    results.write("\t{}\n".format(f.readline().split()[-1]))
                else:
                    results.write("\n")
            f.close()
            results.close()
        else:
            for alg in algs:
                print("{}\t{}\t{}".format(alg, i, alg_chooser(alg, list_of_tasks, num_of_proc)))
                if optymal_present :
                    print("\t{}\n".format(f.readline().split()[-1]))
                else:
                    print("\n")
            f.close()
    return 0

if __name__ == "__main__":
    main()
    