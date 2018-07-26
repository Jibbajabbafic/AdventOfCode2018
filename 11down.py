import math

def solution(a):
    count = 0

    for x in range(10,a+1):
        # print("Checking squares in: ", x)
        x_str = str(x)

        for i in range(len(x_str)):
            num = int(x_str[:i] + x_str[i+1:])
            if math.sqrt(num).is_integer():
                count += 1
                
    # print(count)
    return(count)

# solution(1234)

