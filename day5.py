'''
591/2083

Part one was cool and done relatively quickly minus small logical errors
Part two took a lot of workshopping to get efficient along with multiple annoying small logic errors

'''

from aoclib import *
from copy import deepcopy
#from collections import
DAY = 5
PART = 2

pInp = get_input(DAY)
ans = 0

seeds = []
inc = -1
maps = [[] for i in range(7)]
cMap = None
for i in pInp:
    if i[:5] == "seeds":
        seeds = list(map(int, i[7:].split(" ")))
        newSeeds = []
        for j in range(0, len(seeds), 2):
            newSeeds.append((seeds[j], seeds[j] + seeds[j+1] - 1))

        seeds = deepcopy(newSeeds)
    elif i != '':
        if cMap == None:
            cMap = inc
        else:
            l = tuple(map(int, i.split(" ")))
            newL = (l[1], l[1]+l[2]-1, l[0]-l[1])
            maps[inc].append(newL)
    else:
        cMap = None
        inc += 1


for i in range(7):
    comRanges = []
    
    while len(seeds) > 0:
        r = seeds.pop(0)
        trans = [j for j in maps[i] if j[0] <= r[0] <= j[1]]
        trans = trans[0] if len(trans) > 0 else False
        if not trans:
            nextRange = [j for j in maps[i] if j[0] > r[0]]
            if len(nextRange) == 0:
                comRanges.append(r)
                continue
            else:
                nextRange = min(nextRange, key=lambda x: x[0])
            if r[1] < nextRange[0]:
                comRanges.append(r)
            else:
                comRanges.append((r[0], nextRange[0] - 1))
                seeds.append((nextRange[0], r[1]))
        else:
            if r[1] <= trans[1]:
                comRanges.append((r[0] + trans[2], r[1] + trans[2]))
            else:
                comRanges.append((r[0] + trans[2], trans[1] + trans[2]))
                seeds.append((trans[1]+1, r[1]))

    seeds = deepcopy(comRanges)


ans = min(seeds, key=lambda x: x[0])[0]
submit(DAY, PART, ans)