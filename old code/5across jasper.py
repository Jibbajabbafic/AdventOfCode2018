def solution(a,b):
    copies = 1

    i = 0
    j = 0

    while i < len(a):
        if a[i] == b[j]:
            # print("Match between A & B: ", i, a[i], j, b[j])
            i += 1
        # else:
            # print("No match A & B: ", i, a[i], j, b[j])
        j += 1

        if j >= len(b):
            copies += 1
            j = 0
            # print("Current copies: ",copies)
    
    print("Total copies: ", copies)
    return(copies)

# A = "xyzzxy"
# B = "xyyz"
# sol: xyz, z, xy, 3 copies!

with open("5across.txt") as f:
    for i, line in enumerate(f):
        if i == 0:
            A = line
        if i == 1:
            B = line

solution(A,B)