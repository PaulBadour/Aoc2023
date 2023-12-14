'''
1623/3543

Part one went fine minus some minor logic bugs
Part two took me forever due to me trying to overcomplecate the problem, ended up being very easy
'''

from aoclib import *
import numpy as np
import sys
from copy import deepcopy
sys.set_int_max_str_digits(10000)
DAY = 14
PART = 2

pInp = get_input(DAY)
ans = 0

pInp = [list(i) for i in pInp]



def sToN(x):
    n = ''
    for i in x:
        for j in i:
            n += '1' if j == '.' else '2' if j == '0' else '3'
    return hex(int(n))



states = []
sBoards = []
states.append(sToN(pInp))
sBoards.append(deepcopy(pInp))
t = None
maxRange = 1000000000
for k in range(maxRange):
    #print(k)
    # north
    for i in range(len(pInp)):
        for j in range(len(pInp[i])):

            off = 0
            while True:
                if pInp[i-off][j] == 'O' and i-off != 0 and pInp[i-1-off][j] == '.':
                    pInp[i-1-off][j] = 'O'
                    pInp[i-off][j] = '.'
                    off += 1
                else:
                    break

    for j in range(len(pInp[0])):
        for i in range(len(pInp)):
            off = 0
            while True:
                if pInp[i][j-off] == 'O' and j-off != 0 and pInp[i][j-1-off] == '.':
                    pInp[i][j-1-off] = 'O'
                    pInp[i][j-off] = '.'
                    off += 1
                else:
                    break

    # south
    for i in range(0, len(pInp))[::-1]:
        for j in range(len(pInp[i])):

            off = 0
            while True:
                if pInp[i+off][j] == 'O' and i+off != len(pInp) - 1 and pInp[i+1+off][j] == '.':
                    pInp[i+1+off][j] = 'O'
                    pInp[i+off][j] = '.'
                    off += 1

                else:
                    break


    for j in range(len(pInp[0]))[::-1]:
        for i in range(len(pInp)):
            off = 0
            while True:
                if pInp[i][j+off] == 'O' and j+off != len(pInp[0]) - 1 and pInp[i][j+1+off] == '.':
                    pInp[i][j+1+off] = 'O'
                    pInp[i][j+off] = '.'
                    off += 1
                else:
                    break
    t = sToN(pInp)

    if t in states:

        break
    else:
        states.append(t)
        sBoards.append(deepcopy(pInp))


startLoop = states.index(t)
endLoop = len(states)

r = endLoop - startLoop

s = ((maxRange - startLoop) % r) + startLoop

b = sBoards[s]

for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] == 'O':
            ans += len(b) - i
submit(DAY, PART, ans)