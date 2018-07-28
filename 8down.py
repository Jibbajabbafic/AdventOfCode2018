# Please write your code inside the function stub below.

def solution(n, m, r, c, k):
    # x_spaces = calc_spaces(r)
    # y_spaces = calc_spaces(c)

    rooms = []

    for i, x in enumerate(r):
        print("x: ", i, x)
        for j, y in enumerate(c):
            print("y: ", j, y)
            if i > 0 and j > 0:
                diff_x = x - r[i-1] - 1
                diff_y = y - c[j-1] - 1
                rooms.append(diff_x * diff_y)
    # print(rooms)
    rooms.sort()
    return(rooms[k-1])

# def calc_spaces(walls):
#     spaces = []
#     for i, wall in enumerate(walls):
#         if i+1 < len(walls):
#             spaces.append(walls[i+1] - wall - 1)
#     return(spaces)

# print(solution(5, 5, (2, 4), (2, 4), 1))