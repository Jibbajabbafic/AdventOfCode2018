# Please write your code inside the function stub below.
import copy

def solution(s):
    count={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
    maxodd=[]
    maxeven=[]
    for i in range(1,7):
        pos=0
        tempmaxeven=[]
        tempmaxodd=[]
        for a in s:
            count[a]+=1
            if oddcount(count)==i:
                tempmaxodd.append(pos)
            if evencount(count)==i:
                tempmaxeven.append(pos)
            pos+=1
        maxodd.append(copy.copy(tempmaxodd))
        maxeven.append(copy.copy(tempmaxeven))
    print(maxodd)
    print(maxeven)
    
    posns=[0,]
    for i in range(5,0,-1):
        if maxodd[i]:
            posns.append(maxodd[i][0])
    for i in range(5,0,-1):
        if maxeven[i]:
            j=0
            while maxeven[i][j]<posns[0]:
                j+=1
            posns.append(maxeven[i][j])
    for i in range(5,0,-1):
        if maxodd[i]:
            j=0
            while maxodd[i][j]<posns[1]:
                j+=1
            posns.append(maxodd[i][j])
    
    posns.append(len(s)-1)
    print(posns)
    
    score=0
    for i in range(4):
        score+=palin(s[posns[i]:posns[i+1]])
    return score    
    
    
def oddcount(count):
    oddcounter=0
    for c in count.values():
        if int(c/2)!=c/2:
            oddcounter+=1
    return oddcounter
    
def evencount(count):
    evencounter=0
    for c in count.values():
        if int(c/2)==c/2 and c!=0:
            evencounter+=1
    return evencounter
    
def palin(astring):
    oddexists=False
    size=0
    count={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
    for a in astring:
        count[a]+=1
    for v in count.values():
        if v/2==int(v/2):
            size+=v
        else:
            oddexists=True
            size+=v-1
    if oddexists:
        size+=1
    return size
        
    
