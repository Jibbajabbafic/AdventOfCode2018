import math

def solution(a):
    count = 0
    for x in range(10,a+1):
        if almst_sqr(x):
            count += 1
    
    return(count)
    
def almst_sqr(y):
    y_str = str(y)
    for i in range(len(y_str)):
        num = int(y_str[:i] + y_str[i+1:])
        if math.sqrt(num).is_integer():
            return(True)