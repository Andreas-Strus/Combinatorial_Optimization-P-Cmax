def set_finder(tasks):
    index=0
    size=0
    for i in range(1,len(tasks)):
            if tasks[i]<tasks[i-1]:
                size +=1
            else:
                for j in range(i-size, i):
                    temp = tasks[index]
                    tasks[index] =tasks[j]
                    tasks[j]=temp
                    index+=1
    return tasks