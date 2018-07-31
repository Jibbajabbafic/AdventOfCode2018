# Please write your code inside the function stub below.
import math as m


def solution(n, c):
    print(c)
    c_array=[]
    for tup in c:
        c_array.append(list(tup))
    c=c_array
    count=0
    change=True
    while(change):
        print(c)
    
        tempc=[]
        for i in range(count+1):
            tempc.append(c[i])
        for j in range(count+1,len(c)):
            other=1
            added=False
            for k in c[j]:
                if k in tempc[count]:
                    tempc.append(c[j,other])
                    added=True
                    break
                else:
                    other-1
            if not added:
                tempc.append(c[j])
        if tempc[count]==c[count]:
            count+=1
        c=tempc
        if count==len(c):
            change=False
    combinations=1
    for a in c:
        combinations*=m.factorial(len(a))
    return combinations%(pow(10,9)+7)

        