'''
1949/1558

Not incredibly challenging, first method of completing was awful and wasted a ton of time
I am shocked part 2 ran in a reasonable amount of time, i was worried about optimization
'''

from aoclib import *
DAY = 16
PART = 2

pInp = get_input(DAY)
ans = 0
grid = [list(i) for i in pInp]

def start(x, y, d):
    locs = [[x,y,d]]
    # 0123 NESW
    l = set()
    starts = []
    while len(locs) > 0:

        dels = []
        for num,i in enumerate(locs):
            match i[2]:
                case 0:
                    locs[num][0] -= 1
                case 1:
                    locs[num][1] += 1
                case 2:
                    locs[num][0] += 1
                case 3:
                    locs[num][1] -= 1
            i = locs[num]
            if i[0] < 0 or i[1] < 0 or i[0] >= len(grid) or i[1] >= len(grid[0]):
                dels.append(i)
                continue

            if (i[0], i[1]) not in l:
                timeout = 0
                l.add((i[0], i[1]))

            match grid[i[0]][i[1]]:
                case '.':

                    pass
                case '/':

                    if i[2] == 0:
                        locs[num][2] = 1
                    elif i[2] == 1:
                        locs[num][2] = 0
                    elif i[2] == 2:
                        locs[num][2] = 3
                    elif i[2] == 3:
                        locs[num][2] = 2

                case "\\":

                    if i[2] == 0:
                        locs[num][2] = 3
                    elif i[2] == 1:
                        locs[num][2] = 2
                    elif i[2] == 2:
                        locs[num][2] = 1
                    elif i[2] == 3:
                        locs[num][2] = 0
                
                case '-':

                    if i[2] in (0,2):
                        dels.append(i)
                        if [i[0], i[1], 1] not in starts:
                            starts.append([i[0], i[1], 1])
                            locs.append([i[0], i[1], 1])
                        if [i[0], i[1], 3] not in starts:
                            starts.append([i[0], i[1], 3])
                            locs.append([i[0], i[1], 3])

                case '|':

                    if i[2] in (1,3):
                        dels.append(i)
                        if [i[0], i[1], 0] not in starts:
                            starts.append([i[0], i[1], 0])
                            locs.append([i[0], i[1], 0])
                        if [i[0], i[1], 2] not in starts:
                            starts.append([i[0], i[1], 2])
                            locs.append([i[0], i[1], 2])

        for i in dels:
            locs.remove(i)

    return len(l)


for i in range(0, len(grid[0])):
    ans = max([ans, start(-1, i, 2)])

for i in range(0, len(grid[0])):
    ans = max([ans, start(len(grid), i, 0)])

for i in range(0, len(grid)):
    ans = max([ans, start(i, -1, 1)])

for i in range(0, len(grid)):
    ans = max([ans, start(i, len(grid[0]), 1)])

#ans = len(l)
submit(DAY, PART, ans)