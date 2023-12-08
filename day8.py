'''
301/2968

Very happy with part 1 speed, was a little sad I did not get slightly higher
Man I am not happy with part 2 and my solution. Tried a much more complicated math approach before lcm
'''

from aoclib import *
import math
DAY = 8
PART = 2

pInp = get_input(DAY)
ans = 0
ins = pInp[0]

nodes = {}
for i in pInp[2:]:
    a = i[:3]
    b = i[7:10]
    c = i[12:15]
    nodes[a] = (b,c)

n = []
for i in nodes.keys():
    if i[2] == 'A':
        n.append(i)


nums = []
for i in n:
    curr = i
    count = 0
    c = 0
    while True:
        count += 1
        curr = nodes[curr][0] if ins[c] == 'L' else nodes[curr][1]

        if curr[2] == 'Z':
            nums.append(count)
            break

        c = c + 1 if c < len(ins) - 1 else 0

ans = math.lcm(*nums)


submit(DAY, PART, ans)