# Please write your code inside the function stub below.

def solution(n, x, r):
    groups = []

    for this_bomb in range(n):
        for subset in groups:
            for bomb in bombs_in_range(this_bomb, x, r):
                if bomb in subset:
                    subset.add(this_bomb)
                    break
            else:
                continue
            break
        else:
            a = set()
            a.add(this_bomb)
            groups.append(a)

    return len(groups)

def bombs_in_range(bomb, bombs, strengths):
    bomb_pos = bombs[bomb]
    range_min = bomb_pos - strengths[bomb]
    range_max = bomb_pos + strengths[bomb]

    return_list = []

    for i in range(len(bombs)):
        if i != bomb:
            if range_min <= bombs[i] <= range_max:
                # Bomb i in range
                return_list.append(i)

    return return_list

n = 4
bombs = [2, 6, 7, 10]
strengths = [1, 3, 2, 5]

print(solution(n, bombs, strengths))