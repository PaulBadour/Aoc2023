'''
328/383

Incredibly happy with both solutions today
Part two only needed to add a little bit more logic to my first solution to make it work
'''

from aoclib import *
DAY = 13
PART = 2

pInp = get_input(DAY)
ans = 0

def diff(x,y):
    c = sum([1 if x[i] != y[i] else 0 for i in range(len(x))])
    return c

maps = []

t = []
for i in pInp:
    if i == '':
        maps.append(t)
        t = []
    else:
        t.append(i)

maps.append(t)

for i in maps:
    found = False
    
    for j in range(len(i[0]) - 1):
        off = 1
        d = False
        while True:
            if j - off + 1 >= 0:
                l = [k[j - off + 1] for k in i]
            else:
                l = None

            if j + off < len(i[0]):
                r = [k[j+off] for k in i]
            else:
                r = None

            if (l == None or r == None) and d:
                found = True
                ans += j + 1
                break

            elif (l == None or r == None):
                break

            if l == r:
                off += 1
            elif diff(l,r) == 1:
                off += 1
                d = True
            else:
                break

        if found:
            break

    if found:
        continue

    for j in range(len(i) - 1):
        off = 1
        d = False
        while True:
            if j - off + 1 >= 0:
                l = i[j - off + 1]
            else:
                l = None

            if j + off < len(i):
                r = i[j+off]
            else:
                r = None

            if (l == None or r == None) and d:
                found = True
                ans += (j + 1) * 100
                break
            elif (l == None or r == None):
                break
            if l == r:
                off += 1
            elif diff(l,r) == 1:
                off += 1
                d = True
            else:
                break

        if found:
            break

submit(DAY, PART, ans)
