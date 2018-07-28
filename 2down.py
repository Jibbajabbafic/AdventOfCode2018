# Please write your code inside the function stub below.

def solution(s):
    count=0
    for i in range(6,len(s)+1):
        block ={'Y':0,'R':0,'B':0}
        for char in s[:i]:
            block[char]+=1
        if checker(block):
            count+=1
        for j in range(0,len(s)-i):
            block[s[j]]-=1
            block[s[j+i]]+=1
            if checker(block):
                count+=1
    return count+10000

def checker(block):
    if block['R']!=block['Y'] and block['R']!=block['B'] and block['Y']!=block['B'] and 0 not in block.values():
        return True
    else:
        return False