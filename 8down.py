# Please write your code inside the function stub below.

import bisect

def solution(n, m, r, c, k):

    sorted_rooms = []
    
    total_rooms = (len(r)-1) * (len(c)-1)
    print("Total rooms: ", total_rooms)
    if k > total_rooms/2:
        print("Finding largest rooms...")
        K = 1 + total_rooms - k

        last_x = None
        last_y = None

        for x in r:

            if last_x == None:
                last_x = x
                continue

            if x != last_x:
                diff_x = x - last_x - 1

            for y in c:
                if last_y == None:
                    last_y = y
                else:
                    if y != last_y:
                        diff_y = y - last_y - 1

                    area = diff_x * diff_y

                    if len(sorted_rooms) < K:
                        # list is still shorter than K so add value automatically and keep list sorted
                        bisect.insort(sorted_rooms, area)
                    elif sorted_rooms[0] < area:
                            # smallest value in list is smaller than area, so get rid and add new sorted value
                            del sorted_rooms[0]
                            bisect.insort(sorted_rooms, area)

                    last_y = y
            last_x = x
        return(sorted_rooms[0])
    else:
        # find kth smallest values
        print("Finding smallest rooms...")

        last_x = None
        last_y = None

        for x in r:

            if last_x == None:
                last_x = x
                continue

            if x != last_x:
                diff_x = x - last_x

            for y in c:
                
                if last_y == None:
                    last_y = y

                if y != last_y:
                    diff_y = y - last_y

                area = diff_x * diff_y

                if len(sorted_rooms) < k:
                    # list is still shorter than k so add value automatically and keep list sorted
                    bisect.insort(sorted_rooms, area)
                elif sorted_rooms[k-1] > area:
                        # largest value in list is greater than area, so get rid and add new sorted value
                        del sorted_rooms[k-1]
                        bisect.insort(sorted_rooms, area)

                last_y = y
            last_x = x
        return(sorted_rooms[k-1])

# print(solution(5, 5, (2, 4), (2, 4), 1))